import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type': 'application/json',
          'trainer_token': 'e1c0f898ed994ef67cf6120a0f793b62'}
trainer_id = '4144'

def test_status_code():
    response = requests.get(url = f'{url}/trainers', headers = header)
    assert response.status_code == 200

def test_trainer_id():
    response_trainer = requests.get(url = f'{url}/trainers', headers = header, params={'trainer_id': trainer_id})
    assert response_trainer.json()['data'][0]['id'] == '4144'