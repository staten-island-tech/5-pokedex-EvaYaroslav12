import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

import json
## Open the JSON file of pokemon data
typing = open("./types.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
tipes = json.load(typing)

import json
## Open the JSON file of pokemon data
Movi = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
moves = json.load(Movi)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

def funct (data2):
    a = [d['name']['english'] for d in data2]
    print (a)
# funct(data)

languages = ['english,', 'japanese', 'chinese', 'french']
def langnum (data2):
    a = [d['id'] for d in data2]
    inp = input ('what number pokemon do you want to see? ')
    imp = int(inp)
    if (imp) < 810 and (imp) > 0:
        lang = input ('what language would you like? [enlgish, japanese, chinese, french] ')
        print (data[a.index(imp)]['name'][lang])
# langnum(data)

def typey (data2):
    found = False
    inp = input ('what type would you like to see? ')
    for d in data2:
        if inp in d['type']:
            print(d['name']['english'], d['type'])
            found = True
    if found == False:
        print ('type not found')
        
# typey(data)

def pokesearch (data2):
    found = False
    inp = input ('what pokemon would you like to see? (case sensitive) ')
    for d in data2:
        if inp in d['name']['english']:
            print(d['name']['english'], d['type'])
            found = True
    if found == False:
        print ('pokemon not found')

# pokesearch(data)

def pokemoves (data2, moves2):
    found = False
    inp = input ('what pokemon\'s moves would you like to see? (case sensitive) ')
    for d in data2:
        if inp in d['name']['english']:
            tipe = list(d['type'])
            found = True
            print('found')
            print(tipe)
            if tipe in moves['type']:
                print(moves2)
    if found == False:
        print ('pokemon not found')
pokemoves(data, moves)