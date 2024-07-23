import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = '6fd32a2e14b947237c1b626441821e2c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4116

def test_status_code():
    response = requests.get (url= f'{URL}/v2/pokemons',params ={'trainer_id':TRAINER_ID})
    assert response.status_code == 200
    