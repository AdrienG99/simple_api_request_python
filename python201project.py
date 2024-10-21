#Created by Adrien Grant Jr.
#Small Project to request and retrieve information from a website
#Python 201 project from 2024 Web Development Bootcamp by Kalob Taulien

import requests

#Finding out which pokemon we want info about
pokemon = input("Please enter the name of your favorite pokemon! ")

#adding pokemon name to url to request from website
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
req = requests.get(url)
if req.status_code == 200:
#Bringing JSON into code to get information.
    poke = req.json()

    print("\nHere are some details about your favorite pokemon!")

#Printing out name, ability/ies and type/s
    print("\nTheir name is", poke['name'])

    print("\nTheir main abilities are:")

    for ability in poke['abilities']:
        print(ability['ability']['name'])

    print("\nTheir type/s:")

    for types in poke['types']:
        print(types['type']['name'])
else:

    print("Pokemon not found")


input("\nPress enter to exit")
