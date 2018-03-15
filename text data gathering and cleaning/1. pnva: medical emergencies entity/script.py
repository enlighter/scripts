import json
from pprintpp import pprint

with open('terms.txt') as terms_file:
	lines = terms_file.readlines()

main_list = list()
current = dict()

for term in lines:
	if 'head:' in term:
		if current:
			main_list.append(current)
		term = term.strip()
		term = term.strip('head:')
		term = term.strip()
		current = dict()
		current['value'] = term + ' emergency'
		current['synonyms'] = list()
	else:
		term = term.strip()
		if term:
			current['synonyms'].append(term)

if current:
	main_list.append(current)

pprint(main_list)

with open('data.json', 'w') as data_file:
	json.dump(main_list, data_file)