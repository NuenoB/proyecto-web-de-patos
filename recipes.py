#!/usr/bin/env python

import re
import pprint

drecipte = {'type': '', 'upperleft': '(None)','middleleft':'(None)','lowleft':'(None)',
        'uppermiddle': '(None)','middlemiddle':'(None)','lowmiddle':'(None)','upperright': '(None)','middleright':'(None)','lowright':'(None)','result' :''}

def read_recipie_log():
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
            return  line_recipe
def main():
        line_recipe = read_recipie_log()
        recipies = []
        def parseingre(dr,coordinates):
            if  dr['type'] == "shaped" or dr['type'] == "shapedore":
                w,h = coordinates[0].split(',')
                w = int(w[3:])
                h = int(h[2:-1])
                if w == 3:
                    if h == 3:
                        dr['upperleft'] = coordinates[1]
                        dr['uppermiddle'] = coordinates[2]
                        dr['upperright'] = coordinates[3]
                        dr['middleleft'] = coordinates[4]
                        dr['middlemiddle'] = coordinates[5]
                        dr['middleright'] = coordinates[6]
                        dr['lowleft'] = coordinates[7]
                        dr['lowmiddle'] = coordinates[8]
                        dr['lowright'] = coordinates[9]
                    if h == 2:
                        dr['middleleft'] = coordinates[1]
                        dr['middlemiddle'] = coordinates[2]
                        dr['middleright'] = coordinates[3]
                        dr['lowleft'] = coordinates[4]
                        dr['lowmiddle'] = coordinates[5]
                        dr['lowright'] = coordinates[6]
                    if h == 1:
                        dr['lowleft'] = coordinates[1]
                        dr['lowmiddle'] = coordinates[2]
                        dr['lowright'] = coordinates[3]
                if w == 2:
                    if h ==3:
                        dr['upperleft'] = coordinates[1]
                        dr['uppermiddle'] = coordinates[2]
                        dr['middleleft'] = coordinates[3]
                        dr['middlemiddle'] = coordinates[4]
                        dr['lowleft'] = coordinates[5]
                        dr['lowmiddle'] = coordinates[6]
                    if h ==2:
                        dr['middleleft'] = coordinates[1]
                        dr['middlemiddle'] = coordinates[2]
                        dr['lowleft'] = coordinates[3]
                        dr['lowmiddle'] = coordinates[4]
                    if h ==1:
                        dr['lowleft'] = coordinates[1]
                        dr['lowmiddle'] = coordinates[2]
                if w == 1:
                    if h == 3:
                        dr['upperleft'] = coordinates[1]
                        dr['middleleft'] = coordinates[2]
                        dr['lowleft'] = coordinates[3]
                    if h == 2:
                        dr['middleleft'] = coordinates[1]
                        dr['lowleft'] = coordinates[2]
                    if h == 1:
                        dr['lowleft'] = coordinates[1]
            if  dr['type'] == "shapeless" or dr['type'] == 'shapelessore'  or dr['type'] =='furnace':
                ln = len(coordinates) -1
                templist = ['upperleft', 'uppermiddle' ,'upperright','middleleft','middlemiddle','middleright','lowleft'
                            , 'lowmiddle','lowright']
                while ln >= 0:
                    coordinates[ln]
                    dr[templist[ln]] = coordinates[ln]
                    ln -= 1
            return dr
        for line in line_recipe:
            dr = drecipte.copy()
            dr['type'] = line['type_crafting']
            dr['result'] = line['result']
            dr = parseingre(dr,line['coordinate'])
            recipies.append(dr)
        for r in recipies:
            if r['type'] == 'furnace':
               print (r)



def to_turtle(recipies):
    turtle_list = []
    for recipe in  recipies:
        turtle_list.append(":"+str(recipe['coordinate']) +" :"+recipe['type_crafting']+" :"+str(recipe['result'])+ " ." )
    return turtle_list


if __name__ == '__main__':
    main()
   # with open('data.txt', 'w') as outfile:
   #     for line in to_turtle(line_recipe):
   #         outfile.write(line)
   #         outfile.write('\n')