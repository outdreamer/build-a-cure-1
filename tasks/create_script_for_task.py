def generate_script_for_task(params):
	''' given a task, specify task dependencies in the install.sh script for that task

		- tasks to execute on boot:
			- install elk (including dependencies)
			- install model (dependencies)

		- tasks to execute after boot: 
			- model tasks: 'train', 'deploy_api'
			- elk tasks: 'import', 'start/stop elk', and possibly scheduled bulk operations/queries/reports 

		- to do: 
			- finish 'train_model', 'upload_data', 'deploy_api', 'create_graph' functions
	'''
	commands = []
	all_tasks = ['stop_elastic', 'start_elastic', 'download_model', 'start_api', 'stop_api', 'import_data', 'train_model', 'upload_data', 'deploy_api', 'create_graph']
	if task == 'import_data':
		commands = [
			"data = json_to_csv()",
			"if data:",
			"\tprint('len data to import', len(data))",
			"\timport_ratio = import_to_elk('fgt_event', data, '/data/event/')",
		]
	elif task == 'train_model':
		commands = ["model_path = apply_algorithm(params['data'], params['algorithm'])"]
	elif task == 'upload_data':
		commands = ["uploaded = upload_data(client, connection, instance_name, params['filename'], params['target_dir'])"]
	elif task == 'deploy_api':
		commands = ["deployed = deploy_api(params['model_path'])"]
	elif task_type == 'create_graph':
		''' this should have params like data set, dependent var, graph type, which we'll translate to matplotlib graph layers, axis labels, etc '''
		commands = "graphed = graph_data(client, connection, instance_name, params['graph_type'])"
	else:
		print('unsupported task', params)
	if params['task'] in ['elk', 'model']:
		open_ports = ['9200', '5601'] if params['task'] == 'elk' else ['80']
		home_dir = '/home/ec2-user' if params['cloud'] == 'aws' else '~'
		init_packages = ['java-1.8.0-openjdk-devel', 'git', 'epel-release', 'python3-pip', 'firewalld'] if params['task'] == 'elk' else ['git', 'epel-release', 'python3-pip', 'firewalld']
		all_commands = {}
		if params['task'] == 'model':
			all_commands['xgboost'] = [
				'cd ~/ && git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost'
				'make' # make -j4, cp make/minimum.mk ./config.mk
				'cd python-package && python3 setup.py install --user'
			]
		if params['task'] == 'elk':
			service_packages = ['elasticsearch', 'logstash', 'kibana']
		all_commands['init'] = [''.join(['yum install ', '_'.join(init_packages), '-y'])]
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
		all_commands['service'] = [''.join(['yum install ', '_'.join(service_packages), '-y'])]
		steps = {'firewalld': ['enable']}
		if params['task'] == 'elk':
			steps['elasticsearch'] = ['enable', 'start']
			steps['kibana'] = ['enable', 'start']
		all_commands['config'] = ["sudo systemctl daemon-reload"]
		all_commands['config'].extend([''.join(["systemctl ", ccommand, " ", service]) for service, steps in steps.items() for ccommand in steps])
		all_commands['config'].append(['reboot'])
		all_commands['firewall'] = [''.join(['firewall-cmd --permanent --add-port ', port, '/tcp']) for port in open_ports].append('firewall-cmd --reload')
		if params['task'] == 'elk':
			all_commands['tasks'] = [''.join(['cd ', home_dir, ' && cd ./build-a-cure/tasks && python3 test_import.py'])]
			all_commands['test'] = ['curl -X GET http://localhost:9200/_cat/indices?v']
			all_commands['cleanup_task'] = ['curl -XDELETE http://localhost:9200/fgt_event']
			# get indexes: curl -X GET http://localhost:9200/_aliases
			# search index: curl -X GET http://localhost:9200/fgt_event/_search
			# import one: curl -XPUT 'http://localhost:9200/fgt_event/doc/1' -H 'Content-Type: application/json' -d '{"command": "DHCP statistics3"}'
			# delete index: curl -XDELETE http://localhost:9200/fgt_event
			# import schema: sudo curl -XPUT 'http://127.0.0.1:9200/_template/sample' -d@~/sample.template.json
		for command_type in ['init', 'repo', 'yum_repo', 'service', 'config', 'firewall', 'task', 'test', 'cleanup_task']:
			if command_type in all_commands:
				if len(all_commands[command_type]) > 0:
					commands.extend(all_commands[command_type])

	if len(commands) > 0:
		open(params['task_script_path'], 'w').write('\n'.join(commands))
		return params['task_script_path']
	return False