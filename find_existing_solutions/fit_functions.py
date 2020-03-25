def get_relationship_between_objects(source, target):
	print('function::get_relationship_between_objects')
	join_keyword = 'in order to'
	brief_join_keyword = get_brief_keyword(join_keyword)
	if brief_join_keyword:
		return brief_join_keyword
	return join_keyword

def get_brief_keyword(keyword):
	print('function::get_brief_keyword')
	''' whats the relationship between keywords 'function' and 'input'? intent (you use the input to trigger the function) '''
	return 'to'