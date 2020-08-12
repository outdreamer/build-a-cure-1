import os, json, elasticsearch

'''

config:

curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings -d '{ "transient": { "cluster.routing.allocation.disk.threshold_enabled": false } }'

curl -X PUT "localhost:9200/_all/_settings" -H 'Content-Type: application/json' -d'{ "index.blocks.read_only_allow_delete" : false } }'

'''

def import_entries():
	entries = get_entries()
	if entries:
		print('entries', entries.keys())
		es = elasticsearch.Elasticsearch(
		    ['localhost'],
		    port=9200
		)
		if es:
			for file_type in entries:
				print('importing', file_type)
				file_type_name = ''.join([file_type, '.json'])
				with open(file_type_name, 'w') as f:
					print('entries[file_type]', file_type, entries[file_type])
					print('entries[file_type]', type(entries[file_type]))
					'''
					try:
						json.dump(f, entries[file_type])
					except Exception as e:
						print('json write failed for data', e, entries[file_type])
						entry_lines = []
						for entry in entries[file_type]:
							entry = ''.join([':'.join([k, v]) for k, v in entry.items()])
							entry_lines.append(entry)
						if len(entry_lines) > 0:
							f.write('\n'.join(entry_lines))
					f.close()
					'''
				for i, entry in enumerate(entries[file_type]):
					doc_type = 'event' if 'fgt' in file_type else 'email'
					try:
						es.index(index=file_type, id=i, body=entry)
					except Exception as e:
						print('elastic', e)
			return True
	return False

def get_entries():
	entries = {}
	cwd = os.getcwd()
	origin_path = ''.join([cwd, '/data/'])
	print('path', origin_path)
	for subdir in ['email', 'event']:
		path = ''.join([origin_path, subdir])
		for dirname in os.listdir(path):
			full_dirname = ''.join([path, '/', dirname])
			print('dirname', full_dirname)
			if os.path.isdir(full_dirname):
				for cur, _dirs, files in os.walk(full_dirname):
					for filename in files:
						filename = ''.join([cur, '/', filename])
						file_type = 'fgt_event' if 'fgt_event' in filename else 'fgt_traffic' if 'fgt_traffic' in filename else 'email'
						if file_type not in entries:
							entries[file_type] = [] 
						print('filename', filename)
						data = get_data(filename)
						if data:
							if type(data) == list:
								entry = add_to_entries(data)
								if entry:
									entries[file_type].append(entry)
							else:
								for row in data:
									entry = row['result'] if 'result' in row else row						
									entries[file_type].append(entry)
			else:
				file_type = 'fgt_event' if 'fgt_event' in full_dirname else 'fgt_traffic' if 'fgt_traffic' in full_dirname else 'email'
				if file_type not in entries:
					entries[file_type] = [] 
				data = get_data(full_dirname)
				if data:
					if type(data) == list:
						entry = add_to_entries(data)
						if entry:
							entries[file_type].append(entry)
					else:
						for row in data:
							entry = row['result'] if 'result' in row else row
							entries[file_type].append(entry)
	if entries:
		print('entries', len(entries))
		for key in entries:
			print('key', len(entries[key]))
			for entry in entries[key]:
				for k, v in entry.items():
					print('k', k, ' : ', v)
		return entries
	return Falsee

def add_to_entries(data):
	entry = {}	
	content = []
	for i, line in enumerate(data):
		if i > 0: # skip first line
			delimiter = '\n\n' if '\n\n' in data else '<HTML>' if '<HTML>' in data else '<html>'
			data_split = '\n'.join(data).split(delimiter) 
			if len(data_split) == 2:
				fields = data_split[0]
				entry['content'] = ''.join(['<HTML>', data_split[1]]) if '<HTML>' in data else ''.join(['<html>', data_split[1]]) if '<html>' in data else data_split[1]
				total_line = [fields]
				next_data = data[i:]
				for j, next_line in enumerate(next_data):
					if next_line.count('\t') > line.count('\t'):
						# add next lines until you find 
						total_line.append(next_line)
				if len(total_line) > 1:
					line = '\n'.join(total_line)
				if ':' in line:
					tags = ['a', 'html', 'p', 'span', 'table', 'th', 'tr', 'td']
					for tag in tags:
						if ''.join(['<', tag, ' ']) in line or ''.join(['<', tag, '>']) in line:
							print('content line', line)
							content.append(line)
					else: 
						''' key: value metadata '''
						line_fields = line.split(':')
						entry[line_fields[0]] = line_fields[1].strip()
			else:
				print('content delimiter not found for email', data)
	if len(content) > 0:
		print('content', content)
		entry['content'] = '\n'.join(content)
	if entry:
		return entry
	return False

def get_data(file_path):
	if os.path.exists(file_path):
		objects = None
		with open(file_path, 'r') as f:
			if 'DS_Store' not in file_path:
				if '.json' in file_path:
					try:
						objects = json.load(f)
					except Exception as e:
						print('load', e)
				else:
					try:
						objects = f.read().split('\n')
					except Exception as e:
						print('read', e)
					if objects:
						print('objects', len(objects))
			f.close()
		if objects:
			return objects
	return False


import_entries()