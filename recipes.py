#!/usr/bin/env python

import re
import pprint

line_recipe =[]
def main():
	with open('vsdump-2015-07-17T143500-recipes.log') as f:
		lines = f.readlines()
		for line in lines:
			dict_recipie = {'type_crafting':'', 'coordinate':[] ,'result':''}
			coordinates = line.split('!')[1].split('->')[0]
			for coor in (re.findall(r"\([^\)]*\)",coordinates)):
				dict_recipie['coordinate'].append(coor)
			dict_recipie['type_crafting'] = (line.split('!')[0].split(':')[1])
			dict_recipie['result'] = line.split('!')[1].split('->')[1][:-1]
			line_recipe.append(dict_recipie)

if __name__ == '__main__':
	main()
	for l in line_recipe:
		print(l)
