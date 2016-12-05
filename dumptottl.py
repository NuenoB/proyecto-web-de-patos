#!/usr/bin/env python
# -*- coding: latin-1 -*-

import re
#%%
def main():
    #%%
    str_itemname="vsdump-2015-07-17T143502-items.log"
    arc_itemname = open(str_itemname)
    line=arc_itemname.readline()
    item_dics=dict()
    while line != '':
		# procesar lin
        m = re.search("recipedumper:item!(\d+):(\d+) (.*)", line)
        name=line.split("||")[1]
        name=name[2:]
        id_item=int(m.group(1))*pow(10,len(m.group(2)))+int(m.group(2))
        item_des=dict()
        item_des={"name":name,"id":id_item,"id_1":m.group(1),"id_2":m.group(2),
                  "name_intern":m.group(3)}
        item_dics[id_item]=item_des
        line=arc_itemname.readline()
    #%%
    str_itemname="vsdump-2015-07-17T143502-oredict.log"
    arc_itemdict = open(str_itemname)
    line=arc_itemdict.readline()
    item_dics_oredictinary=dict()
    while line != '':
        gr=line.split("!")
        rel=gr[1].split("->")
#        print(rel[0] + " " + rel[1])
        ms = rel[1].split(")")
        tl=[]
        for m in ms:
            if not m =='\n':
                n_str=m[1:]
                n_str2=n_str.split(",")
                n_gr=n_str2[0].split(":")
                temp_str=n_gr[0]+n_gr[1]
                print(temp_str)
                n_int=int(n_gr[0]+n_gr[1]) 
                tl.append(n_int)
        item_dics_oredictinary[rel[0]]=tl
        line=arc_itemdict.readline()
        #%%
	line_recipe =[]
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
#%%
    to_archive="@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n @prefix : <http://example.com/> .\n"
    for l in line_recipe:
        p_n_gr=l["result"].split(",")[0][1:]
        n_gr=p_n_gr.split(":")
        n_int=int(n_gr[0]+n_gr[1]) 
        sujeto=":"+str(n_int)
        to_archive=to_archive+sujeto+' :amount "'+ l["result"].split(",")[1][:-1]+'"^^xsd:integer . \n'
#%%
if __name__ == '__main__':
    main()
#interfase or antologi, external wiki data, rdflib
# demo not screen shot
