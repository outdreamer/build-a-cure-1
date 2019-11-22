# https://libraries.mit.edu/scholarly/publishing/apis-for-scholarly-resources/

# https://dev.elsevier.com/sd_apis.html

'''
https://www.mediawiki.org/wiki/REST_API
https://en.wikipedia.org/api/rest_v1/page/summary/Stack_Overflow
http://export.arxiv.org/api/query?search_query=all:electron
ftp://ftp.ncbi.nlm.nih.gov/
'''
import urllib
from xml.dom.minidom import parse
import xml.dom.minidom
	
# initial output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
# type output should be: ['azole', 'essential oils from plant genus x']
# functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole

keyword = 'cryptococcus'
treatments = get_known_treatments(keyword)

def get_reason(treatment):
	''' get the reason why this worked or failed, meaning the mechanism of action, 
	so you can do searches for other compounds with similar activity '''

def get_role(treatment):
  ''' for fluconazole, this should be "inhibitor of cyp3a4" '''
  ''' the difference between the role and the reason is the 
  reason is a specific process and the role can be more complex '''

def get_other_treatments_with_role(role, original_treatment):
  ''' find other inhibitors of cyp3a4, in addition to fluconazole '''

def get_known_treatments(condition_keyword):
	''' fetch treatments from research studies '''
	just_summary = True
	articles = pull_all_data(condition_keyword, just_summary)
	object_set = set()
	relationships = []
	treatments = []
	for line in articles:
		objects = pull_objects_from_doc(line)
		object_set.add(objects)
		line_relationships = get_relationships(objects)
		relationships.extend(line_relationships)
	for r in relationships:
		outcome = get_outcome_of_relationship(r)
		if outcome == 'positive':
			treatments.append(r)
	return treatments

def get_outcome_of_relationship(relationship):
	''' this processes a relationship like:
	"this protein activates this gene" or "this compound had a synergistic effect"
	and outputs whether this is a positive association for the condition, 
	meaning it can be used as a treatment, or a meaningless one
	'''

def process_entries(entries, just_summary):
	articles = []
	for entry in entries:
		for node in entry:
			if just_summary is True:
				if node.nodeName == 'summary':
					articles.extend(node.nodeValue.split('\n'))
			else:
				article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
				if node.nodeName == 'category':
					article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
				elif node.nodeName in article:
					article[key] = node.nodeValue
				articles.append(article)
	return articles

def pull_all_data(keyword, just_summary):
	''' get data from research study api '''
	start = 0
	total_results = 0
	max_results = 10
	page_number = 1
	articles = []
	for i in range(0, page_number):
		url = ''.join(['http://export.arxiv.org/api/query?search_query=all:', keyword, '&start=', start, '&max_results=', max_results])
		data = urllib.urlopen(url).read()
		print('data', data)
		DOMTree = xml.dom.minidom.parseString(data)
		collection = DOMTree.documentElement #feed
		entries = collection.getElementsByTagName("entry")
		print('entries length', len(entries))
		if total_results == 0:
			total_results = collection.getElementsByTagName("opensearch:totalResults") #.nodeValue
			print('tr', totalResults)
			page_number = ((total_results - max_results) / max_results) + 1
		new_articles = process_entries(entries, just_summary)
		articles.extend(new_articles)
		start = start + len(new_articles)
	with open('articles.txt', 'w') as f:
		f.write(articles)
		f.close()
	return articles

def pull_objects_from_doc(content):
  ''' from a research abstract, this should return the treatment, condition, 
      and inputs/outputs of any functions relating them '''

def get_relationships(objects):
  ''' this should identify the relationships between objects identified in pull_objects_from_doc,
      standardize them, storing them in a dict '''

def is_unique_relationship(relationship, objects):
  ''' check the relationship dict to see if this relationship exists, 
      in a different order or with a different verb '''

def get_synonym(relationship_verb):
  ''' this should standardize a verb like 'enhance' to a verb like 'increase' '''

