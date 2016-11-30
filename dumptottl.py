#!/usr/bin/env python

import re

def main():
	str_itemname="vsdump-2015-07-17T143502-items.log"
	arc_itemname = open(str_itemname)
	line=arc_itemname.readline()
	item_name=dict()
	while line != '':
		# procesar line
		print (line.split("||")[1] )
		m = re.search("recipedumper:item!(\d+):(\d+) U=([a-zA-Z0-9._ :|'-/§]*)\|\|L=([a-zA-Z0-9 '§]*)", line)
		print (str(m.group(1))+" "+str(m.group(2))+" "+str(m.group(3))+" "+str(m.group(4)))

		id_item=int(m.group(1))*pow(10,len(m.group(2)))+int(m.group(2))
		nombre=m.group(4)
		item_name[id_item]=nombre
		print (str(id_item)+" "+str(nombre) + "\n")
		line=arc_itemname.readline()

if __name__ == '__main__':
	print ("hola || chao".split(" || "))
	main()
#interfase or antologi, external wiki data, rdflib
