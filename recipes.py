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
                line_recipe.append((line ,dict_recipie))
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
        for raw,line in line_recipe:
            dr = drecipte.copy()
            dr['type'] = line['type_crafting']
            dr['result'] = line['result']
            dr = parseingre(dr,line['coordinate'])
            recipies.append((raw,dr))
        with open('recipies.ttl', 'w') as outfile:
          def writeline ():
              outfile.write("\n")
          outfile.write("@prefix foaf: <http://xmlns.com/foaf/0.1/> .")
          writeline()
          outfile.write ("@prefix : <http://example.com/> .")
          writeline()
          writeline()
          for raw,dict in recipies:
                to_turtle (outfile ,dict,raw)



def to_turtle(out,recipie,raw):
    raw = raw[13:-1]
    def writethe9Ingredients(out,recipie,raw):
        out.write (":" + recipie['upperleft'] + " :UpperLeftIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['middleleft'] + " :MiddleLeftIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['lowleft'] + " :LowLeftIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['uppermiddle'] + " :UpperMiddleIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['middlemiddle'] + " :MiddleMiddleIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['lowmiddle'] + " :LowMiddleIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['upperright'] + " :UpperRightIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['middleright'] + " :MiddleRightIngredientOf " + ":" + raw +"\n"  )
        out.write (":" + recipie['lowright'] + " :LowRightIngredientOf " + ":" + raw +"\n"  )

    def writeonlynotNull(out,recipie,raw):
        if recipie['upperleft'] != "(None)":
            out.write (":" + recipie['upperleft'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['middleleft'] != "(None)":
            out.write (":" + recipie['middleleft'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['lowleft'] != "(None)":
            out.write (":" + recipie['lowleft'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['uppermiddle'] != "(None)":
            out.write (":" + recipie['uppermiddle'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['middlemiddle'] != "(None)":
            out.write (":" + recipie['middlemiddle'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['lowmiddle'] != "(None)":
            out.write (":" + recipie['lowmiddle'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['upperright'] != "(None)":
            out.write (":" + recipie['upperright'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['middleright'] != "(None)":
            out.write (":" + recipie['middleright'] + " :IngredientOf " + ":" + raw +"\n"  )
        if recipie['lowright'] != "(None)":
            out.write (":" + recipie['lowright'] + " :IngredientOf " + ":" + raw +"\n"  )

    if recipie['type'] == "shaped":
            out.write (":" + raw + " a :ShapedRecipe \n"  )
            writethe9Ingredients(out,recipie,raw)
    if recipie['type'] == "shapeless":
            out.write (":" + raw + " a :ShapelessRecipe \n"  )
            writeonlynotNull(out,recipie,raw)
    if recipie['type'] == "shapelessore":
            out.write (":" + raw + " a :ShapelessOreRecipe \n"  )
            writeonlynotNull(out,recipie,raw)
    if recipie['type'] == "shapedore":
            out.write (":" + raw + " a :ShapedOreRecipe \n"  )
            writethe9Ingredients(out,recipie,raw)
    if recipie['type'] == "furnace":
            out.write (":" + raw + " a :FurnaceRecipie \n"  )
            writeonlynotNull(out,recipie,raw)
    out.write (":"+ recipie['result'] + " :productOf " +":" + raw + "\n" )
    out.write("\n" )
    out.write("\n" )

if __name__ == '__main__':
    main()
   # with open('data.txt', 'w') as outfile:
   #     for line in to_turtle(line_recipe):
   #         outfile.write(line)
   #         outfile.write('\n')