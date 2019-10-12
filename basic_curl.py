import requests
import json
import csv
import os


def printCSVData(pokeData):
    try:
        with open("file.csv", 'w') as f:
            f.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % ("Pokemon name:", pokeData['name'], "id is:", pokeData['id'], 
            	"weight is:", pokeData["weight"], "height is:", pokeData["height"]))
    except:
        print("Couldn't print to file")

def getData():
	while True:

		pokemon_input = input("Enter a pokemon")

		response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_input +"/")
		respcode = response.status_code

		print(respcode)

		if respcode == 200:

			data = response.json()
			print("The Pokemon: " +  data['name'].upper(), 
				"has an pokedex index of:", data['id'], 
				"It weighs", data['weight'], 
				" and it s height is:" ,data['height'])

			pokemonData = {
			'name' : data['name'].upper(), 
			'id' : data['id'], 
			'weight': data['weight'],
			'height': data['height'] 
			}
			printCSVData(pokemonData)

		else:
			print ("an error occered")

		pokemon_input_again = input("Wout you like to enter another?")

		if pokemon_input_again.lower() not in ('n', 'no' , ''):
			continue
		else:
			print ("Closing Pokedex")
			break

getData()
