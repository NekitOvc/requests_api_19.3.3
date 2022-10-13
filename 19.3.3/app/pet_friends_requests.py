import requests
import json

url = 'https://petstore.swagger.io/v2'

# проверка, есть ли такой пользователь
def get_username(username):
    headers_get = {'accept': 'application/json'}
    res = requests.get(f'{url}/user/{username}', headers=headers_get)
    print(res.status_code)
    print(res.json())

get_username('user') #получаем информацию, есть ли такой пользователь

# добавление нового питомца
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Котопёс"
  },
  "name": "Кот и Пёс",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

def add_new_pet(body):
    headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data_post = json.dumps(body).encode('utf-8')
    res = requests.post(f'{url}/pet', headers=headers_post, data=data_post)
    print(res.status_code)
    return  res.json()

added_pet = add_new_pet(new_pet)
print(added_pet)
petid = added_pet['id']

# внесение изменений в добавленного питомца
modified_pet = {
  "id": petid,
  "category": {
    "id": 0,
    "name": "Лев"
  },
  "name": "Алекс",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

def update_pet(body):
    headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data_put = json.dumps(body).encode('utf-8')
    res = requests.put(f'{url}/pet', headers=headers_put, data=data_put)
    print(res.status_code)
    print(res.json())

update_pet(modified_pet)

# удаление питомца
def delete_pet(pet_id):
    headers_delete = {'accept': 'application/json'}
    res = requests.delete(f'{url}/pet/{pet_id}', headers=headers_delete)
    print(res.status_code)

delete_pet(petid)
