import requests
import json

def getData():
	while True:

		pokemon_input = input("Enter a pokemon")

		response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_input +"/")
		respcode = response.status_code

		print(respcode)

		if respcode == 200:

			data = response.json()
			print("The Pokemon: " +  data['name'].upper() , "has an pokedex index of:" , data['id'], "It weighs", data['weight'], " and it s height is:" ,data['height'])

		else:
			print ("an error occered")

		pokemon_input_again = input("Would you like to enter another?")

		if pokemon_input_again.lower() not in ('n', 'no' , ''):
			continue
		else:
			print ("Closing Pokedex")
			break

getData()
