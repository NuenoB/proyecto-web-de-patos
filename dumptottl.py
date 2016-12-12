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
                  "name_intern":m.group(3).split("||")[0][2:]}
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
    tll=open("items.ttl","w")
    tll.write("@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n@prefix : <http://example.com/> .\n\n")
    for l in line_recipe:
        p_n_gr=l["result"].split(",")[0][1:]
        n_gr=p_n_gr.split(":")
        n_int=int(n_gr[0]+n_gr[1]) 
        sujeto=":"+str(n_int)
        tll.write(sujeto +' :amount "'+ l["result"].split(",")[1][:-1]+'"^^xsd:integer . \n')
        tll.write(sujeto +' :typeCrafting '+l["type_crafting"]+' . \n')
        tll.write(sujeto +' :id "'+l["result"].split(":")[0][1:]+'"^^xsd:integer . \n')
        tll.write(sujeto +' :subId "'+l["result"].split(":")[1].split(",")[0]+'"^^xsd:integer . \n')
        tll.write(sujeto +' foaf:name '+item_dics[n_int]['name'][:-1]+' . \n')
        
        for c in l["coordinate"]:
            if "w=" in c:
                #print(c)
                tll.write(sujeto +' :w '+c.split(",")[0].split("=")[1] + ". \n")
                #print(c.split(",")[0].split("=")[1])
                tll.write(sujeto +' :h '+c.split("=")[2].split(")")[0] + ". \n")
            elif "@" in c:
                #print(c)
                name=c.split(",")[0][1:]
                tll.write(sujeto +' :craftwith '+ name + " . \n")
            elif "None" in c:
                pass
            else:
                print(c)
                c_p_n_gr=c.split(",")[0][1:]
                c_n_gr=c_p_n_gr.split(":")
                c_n_int=int(c_n_gr[0]+c_n_gr[1]) 
                tll.write(sujeto +' :craftwith '+ str(c_n_int) + " . \n")
                
        tll.write("\n")
#%%
    line_recipe =[]
    log=open("recipes.log","w")
    with open('vsdump-2015-07-17T143500-recipes.log') as f:
        lines = f.readlines()
        for line in lines:
            pass
    
#%%
if __name__ == '__main__':
    main()
#interfase or antologi, external wiki data, rdflib
# demo not screen shot
