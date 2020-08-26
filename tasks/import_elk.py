import os, json, elasticsearch

'''
config:
	curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings -d '{ "transient": { "cluster.routing.allocation.disk.threshold_enabled": false } }'
	curl -X PUT "localhost:9200/_all/_settings" -H 'Content-Type: application/json' -d'{ "index.blocks.read_only_allow_delete" : false } }'

test:
	# get indexes: curl -X GET http://localhost:9200/_aliases
	# search index: curl -X GET http://localhost:9200/fgt_event/_search
	# import one: curl -XPUT 'http://localhost:9200/fgt_event/doc/1' -H 'Content-Type: application/json' -d '{"command": "DHCP statistics3"}'
	# delete index: curl -XDELETE http://localhost:9200/fgt_event
	# import schema: sudo curl -XPUT 'http://127.0.0.1:9200/_template/sample' -d@~/sample.template.json

cleanup:
    curl -XDELETE http://localhost:9200/fgt_event
'''

def connect_to_es(params):
	es = elasticsearch.Elasticsearch(
		[params['es_host']],
		port=9200
	)
	if es:
		return es
	return False

def import_to_elk(params):
	es = connect_to_es(params)
	if es:
		import_count = 0
		if 'data' not in params:
			origin_path = ''.join([os.getcwd(), params['data_path']]) # path = '/data/event/'
			for cur, _dirs, files in os.walk(origin_path):
				for original_filename in files:
					filename = ''.join([cur, '/', original_filename])
					if '.json' in filename and 'new_' not in filename:
						with open(filename, 'r') as f:
							for i, line in enumerate(f):
								line_data = json.loads(line)
								if line_data:
									if 'result' in line_data:
										record = {}
										for key, val in line_data['result'].items():
											if '_' == key[0]:
												record[key[1:]] = val
											else:
												record[key] = val
										try:
											es.index(index=params['index_name'], id=i, body=record)
											import_count ++ 1
										except Exception as e:
											print('elastic import', e)
			return import_count
		else:
			if len(params['data']) > 0:
				for i, line in enumerate(params['data']):
					try:
						print('indexing', params['index_name'], i, line)
						es.index(index=params['index_name'], id=i, body=line)
						import_count ++ 1
					except Exception as e:
						print('elastic import', e)
				return import_count
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