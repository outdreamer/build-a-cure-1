import os

def generate_script_for_task(params):
	''' given an install task, specify task dependencies & commands in the install.sh script for that task '''
	print('generate_script_for_task: ', params['task'], ' at task script path', params['task_script_path'])
	commands = ["#!/bin/bash"] if '.sh' in params['task_script_path'] else []
	if params['task'] in ['elk', 'model']:
		open_ports = ['9200', '5601'] if params['task'] == 'elk' else ['80']
		home_dir = '/home/ec2-user' if params['cloud'] == 'aws' else '~'
		init_packages = ['git', 'wget', 'epel-release', 'python3', 'python3-pip', 'firewalld']
		if params['task'] == 'elk':
			init_packages.append('java-1.8.0-openjdk-devel')
		if params['task'] == 'model':
			init_packages.extend(['centos-release-scl', 'devtoolset-7-gcc*', 'gcc-c++', 'cmake3']) # GCC version must be at least 5.0!
		all_commands = {}
		if params['task'] == 'model':
			# https://xgboost.readthedocs.io/en/latest/build.html#building-on-linux-distributions
			all_commands['xgboost'] = [
				'scl enable devtoolset-7 bash',
				'export CC=/opt/rh/devtoolset-7/root/usr/bin/gcc',
				'export CXX=/opt/rh/devtoolset-7/root/usr/bin/g++',
				'cd ~/ && git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost',
				'mkdir build && cd build',
				'cmake3 -D CMAKE_C_COMPILER=/opt/rh/devtoolset-7/root/usr/bin/gcc -D CMAKE_CXX_COMPILER=/opt/rh/devtoolset-7/root/usr/bin/g++ ..',
				'make -j4',
				'cd ../python-package && python3 setup.py install --user'
			]
		if params['task'] == 'elk':
			service_packages = ['elasticsearch', 'logstash', 'kibana']
		all_commands['init'] = [''.join(['yum install ', ' '.join(init_packages), ' -y'])]
		all_commands['repo'] = [''.join(["cd ", home_dir, " && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/tasks && pip3 install -r ", params['task'], "_requirements.txt"])]
		if params['task'] == 'elk':
			all_commands['repo'].extend([
				"cp ./modified_original/new_async_init.py /usr/local/lib/python3.6/site-packages/elasticsearch/_async/client/__init__.py",
				"cp ./modified_original/new_client_init.py  /usr/local/lib/python3.6/site-packages/elasticsearch/client/__init__.py"
			])
		all_commands['yum_repo'] = ['rpm –import https://artifacts.elastic.co/GPG-KEY-elasticsearch']
		if params['task'] == 'elk':
			for service in ['elasticsearch', 'logstash', 'kibana']:
				all_commands['yum_repo'].extend([
					''.join(['echo "[', service, ']" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "name=', service, '" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "baseurl=https://artifacts.elastic.co/packages/6.x/yum" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "gpgcheck=1" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "gpgkey=http://artifacts.elastic.co/GPG-KEY-elasticsearch" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "enabled=1" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "autorefresh=1" >> /etc/yum.repos.d/', service, '.repo']),
					''.join(['echo "type=rpm-md" >> /etc/yum.repos.d/', service, '.repo'])
				])
		all_commands['service'] = [''.join(['yum install ', ' '.join(service_packages), ' -y']), "echo 'server.host: \"0.0.0.0\"' >> /etc/kibana/kibana.yml"]
		steps = {'firewalld': ['enable']}
		if params['task'] == 'elk':
			steps['elasticsearch'] = ['enable', 'start']
			steps['kibana'] = ['enable', 'start']
		all_commands['config'] = ["systemctl daemon-reload"]
		all_commands['config'].extend([''.join(["systemctl ", ccommand, " ", service]) for service, steps in steps.items() for ccommand in steps])
		if len(open_ports) > 0:
			all_commands['firewall'] = [''.join(['firewall-cmd --permanent --add-port ', port, '/tcp']) for port in open_ports]
			all_commands['firewall'].append('firewall-cmd --reload')
		# all_commands['final'] = [] # ['reboot']
		if params['task'] == 'elk':
			all_commands['test'] = [''.join(['sleep 60 && cd ', home_dir, '/build-a-cure/tasks && python3 task__test_import.py >> import.txt && curl -X GET http://localhost:9200/_cat/indices?v >> curl.txt'])]
		for command_type in ['init', 'repo', 'yum_repo', 'service', 'config', 'firewall', 'test']:
			if command_type in all_commands:
				if all_commands[command_type] is not None:
					if len(all_commands[command_type]) > 0:
						print('all_commands[command_type]', all_commands[command_type])
						for command in all_commands[command_type]:
							print('command', command)
							commands.append(command)
	if len(commands) > 0:
		open(params['task_script_path'], 'w').write('\n'.join(commands))
		return params['task_script_path']
	return False