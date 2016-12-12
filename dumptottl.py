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
        item_dics[str(m.group(1)+":"+m.group(2))]=item_des
        line=arc_itemname.readline()
    #%%
    str_itemname="vsdump-2015-07-17T143502-oredict.log"
    arc_itemdict = open(str_itemname)
    line=arc_itemdict.readline()
    item_dics_oredictinary=dict()
    while line != '':
        gr=line.split("!")
        rel=gr[1].split("->")
        print(rel[0] + " " + rel[1])
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
    for key in item_dics:
        l=item_dics[key]
        sujeto=":"+str(l['name_intern'])
        tll.write(sujeto +' :id "'+l["id_1"]+'"^^xsd:integer . \n')
        tll.write(sujeto +' :subId "'+l["id_2"]+'"^^xsd:integer . \n')
        tll.write(sujeto +' foaf:name "'+l['name'][:-1]+'" . \n')
        tll.write(sujeto +' :name_intern "'+l['name_intern']+'" . \n')
                        
        tll.write("\n")
    tll.close()
#%%
    line_recipe =[]
    log_archive=open("recipes.log","w")
    m=0
    with open('vsdump-2015-07-17T143500-recipes.log') as f:
        lines = f.readlines()
        for line in lines:
            ln=s1[0]+"!"
#            re.search("recipedumper:(\d*)!  ((\d+):(\d+)) (.*)", line)
            s1=line.split("!")
            s2=s1[1].split("->")
            s3=s2[1].split(",")
            n_res=s3[1]
            n_gr=s3[0][1:].split(":")
            n_int_res=int(n_gr[0]+n_gr[1])
            res=s2[0].split(")")
            lsl=[]
            for r in res:
                if "w" in r:
                    lsl.append([r+")"])
                elif "@" in r:
                    lr=[]
                    s3=r[1:].split(",")
                    id_n=item_dics_oredictinary[s3[0]]
                    for valor in item_dics_oredictinary[s3[0]]:
                        lr.append("("+item_dics[valor]["name_intern"]+","+s3[1]+")")
                    lsl.append(lr)
                elif "None" in r:
                    lsl.append(["(None)"])
                elif ""==r:
                    pass
                else:
                    s3=r[1:].split(",")
                    n_gr=s3[0].split(":")
                    n_int=int(n_gr[0]+n_gr[1])
                    lsl.append(["("+item_dics[n_int]["name_intern"]+","+s3[1]+")"])
            
            logs=[""]
            for ln in lsl:
                logs2=logs.copy()
                for log in logs2:
                    logs.remove(log)
                    for l in ln:
                        log2=log + l
                        logs.append(log2)
            for log in logs:
                log=log+"->("+item_dics[n_int_res]["name_intern"]+","+n_res
                log="recipedumper:shapedore!"+log
                log_archive.write(log)
#%%
if __name__ == '__main__':
    main()
#interfase or antologi, external wiki data, rdflib
# demo not screen shot
