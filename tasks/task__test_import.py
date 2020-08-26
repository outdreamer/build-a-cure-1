from sanitize import json_to_csv
from import_elk import import_to_elk

messages = []
index_name = 'fgt_event'
data_path = '/data/test/'
converted = json_to_csv()
if converted:
    imported = import_to_elk(index_name, None, data_path)
    if imported:
	    messages.append(''.join(['finished importing', str(imported)]))
	    es = connect_to_es({'es_host': 'localhost'})
	    if es:
		    res = search_entries(es, None, index_name, None)
		    if res:
		    	messages.append(''.join(['retrieved results', str(res['hits']['total']['value'])]))
		    	for hit in res['hits']['hits']:
			    	messages.append('\n'.join([','.join([k, '::', v]) for k, v in hit.items()]))
		if len(messages) > 0:
			open('messages.txt', 'w').write('\n'.join(messages)
	    		
