import requests

url = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type': 'application/json',
          'trainer_token': 'e1c0f898ed994ef67cf6120a0f793b62'}
body_create = {"name": "generate", "photo_id": 609}

response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": 609
}

response_rename = requests.put(url= f'{url}/pokemons', headers = header, json = body_rename)
print(response_rename.text)


body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response_catch.text)
