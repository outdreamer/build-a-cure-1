from sanitize import json_to_csv
from import_elk import import_to_elk
converted = json_to_csv()
if converted:
    imported = import_to_elk('fgt_event', None, '/data/event/')
    if imported:
	    print('finished importing', imported)
