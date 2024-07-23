import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '6fd32a2e14b947237c1b626441821e2c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
BODY_CREAT = {
    "name": "Автотест",
    "photo_id": 3
}
BODY_Change_Pokemon = {
    "pokemon_id": "44647",
    "name": "AvtoTest",
    "photo_id": 9
}
BODY_add_pokeball = {
    "pokemon_id": "44647"
}

response_creat = requests.post (url = f'{URL}/v2/pokemons', headers = HEADER, json = BODY_CREAT)
print (response_creat.text)

response_change = requests.put (url = f'{URL}/v2/pokemons', headers = HEADER, json = BODY_Change_Pokemon)
print (response_change.text)

response_add_pokeball = requests.post (url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = BODY_add_pokeball)
print (response_add_pokeball.text)