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
    item_dics=dict()
    while line != '':
        gr=line.split("!")
        rel=gr[1].split("->")
        print(rel[0] + " " + rel[1])
        ms = rel[1].split(")")
        print(ms)
        tl=[]
        for m in ms:
            if not m =='\n':
                n_str=m[1:-2]
                n_gr=n_str.split(":")
                temp_str=n_gr[0]+n_gr[1]
                n_int=int(n_gr[0]+n_gr[1]) 
                tl.append(n_int)
        item_dics[rel[0]]=tl
        line=arc_itemdict.readline()
#%%
if __name__ == '__main__':
    main()
#interfase or antologi, external wiki data, rdflib
# demo not screen shot
