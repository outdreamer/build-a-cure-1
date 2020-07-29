import os, json, elasticsearch

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
					json.dump(f, entries[file_type])
					f.close()
				for i, entry in enumerate(entries[file_type]):
					doc_type = 'event' if 'fgt' in file_type else 'email'
					es.index(index=file_type, doc_type=doc_type, id=i, body=entry)
			return True
	return False

def get_entries():
	entries = {}
	cwd = os.getcwd()
	origin_path = ''.join([cwd, '/data'])
	print('path', origin_path)
	for subdir in ['/email', '/event']:
		path = ''.join([origin_path, subdir])
		for dirname in os.listdir(path):
			full_dirname = ''.join([path, '/', dirname])
			print('dirname', full_dirname)
			if os.path.isdir(full_dirname):
				for cur, _dirs, files in os.walk(full_dirname):
					for filename in files:
						filename = ''.join([cur, '/', filename])
						print('filename', filename)
						entries = add_to_entries(filename, entries)
			else:
				entries = add_to_entries(full_dirname, entries)
	if entries:
		print('entries', len(entries))
		exit()
		return entries
	return False

def add_to_entries(filename, entries):
	data = get_data(filename)
	if data:
		print('data', data)
		file_type = 'fgt_event' if 'fgt_event' in filename else 'fgt_traffic' if 'fgt_traffic' in filename else 'email'
		if file_type not in entries:
			entries[file_type] = [] 
		if type(data) == list:
			entry = {}
			for i, line in enumerate(data):
				if i > 0: # skip first line
					data_split = '\n'.join(line).split('\n\n')
					if len(data_split) == 2:
						fields = data_split[0]
						entry['content'] = data_split[1]
						total_line = [fields]
						next_data = data[i:]
						for j, next_line in enumerate(next_data):
							if next_line.count('\t') > line.count('\t'):
								# add next lines until you find 
								total_line.append(next_line)
								'''
								Received: from coolre42375.com ([64.86.155.179]) by dogma.slashnull.org
							    (8.11.6/8.11.6) with SMTP id g7N96hZ17715 for <zzzz@jmason.org>;
							    Fri, 23 Aug 2002 10:06:45 +0100
							    '''
						if len(total_line) > 1:
							line = '\n'.join(total_line)
						if ':' in line:
							line_fields = line.split(':')
							entry[line_fields[0]] = line_fields[1].strip()
			if entry:
				entries[file_type].append(entry)
		else:
			for row in data:
				entry = row['result'] if 'result' in row else row
				entries[file_type].append(entry)
	return entries

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
						print('lines', objects)
			f.close()
		if objects:
			return objects
	return False


import_entries()