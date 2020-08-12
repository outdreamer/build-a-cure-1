import os, json, elasticsearch

'''
config:
	curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings -d '{ "transient": { "cluster.routing.allocation.disk.threshold_enabled": false } }'
	curl -X PUT "localhost:9200/_all/_settings" -H 'Content-Type: application/json' -d'{ "index.blocks.read_only_allow_delete" : false } }'
'''

def connect_to_es():
	es = elasticsearch.Elasticsearch(
		['localhost'],
		port=9200
	)
	if es:
		return es
	return False

def import_to_elk(doc_type, data, data_path):
	es = connect_to_es()
	if es:
		import_count = 0
		if data is None:
			cwd = os.getcwd()
			origin_path = ''.join([cwd, data_path]) # path = '/data/event/'
			for cur, _dirs, files in os.walk(origin_path):
				for original_filename in files:
					filename = ''.join([cur, '/', original_filename])
					if '.json' in filename and 'new_' in filename:
						new_json = ''.join([cur, '/new_', original_filename])
						with open(new_json, 'r') as f:
							lines = []
							for i, line in enumerate(f):
								line_data = json.loads(line)
								data.append(line_data)
							f.close()
		if data:
			for i, line in enumerate(data):
				try:
					es.index(index=doc_type, id=i, body=line)
					import_count ++ 1
				except Exception as e:
					print('elastic import', e)
			return import_count / len(data)
	return False

def get_entry(es, index_name, item_id):
	res = es.get(index=index_name, id=item_id)
	if res:
		if res['hits']['total']['value'] > 0:
			print('results count', res['hits']['total']['value'])
			for hit in res['hits']['hits']:
			    print(hit["_source"])
			return res
	return False

def search_entries(es, keyword, index_name, query):
	''' to do: integrate keyword '''
	query = {"query": {"match_all": {}}} if query is None else query
	res = es.search(index=index_name, body=query)
	if res:
		if res['hits']['total']['value'] > 0:
			print('results count', res['hits']['total']['value'])
			for hit in res['hits']['hits']:
			    print(hit["_source"])
			return res
	return False