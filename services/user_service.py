# services/user_service.py

import requests
from faker import Faker

fake = Faker()

def generate_fake_user():
    new_user = {
        "nome": fake.name(),
        "email": fake.email(),
        "password": fake.password(),
        "administrador": "true"
    }
    print("Gerando dados...")
    print("nome -> ", new_user["nome"])
    print("email -> ", new_user["email"])
    print("password -> ", new_user["password"])
    print("administrador -> ", new_user["administrador"])
    return new_user

def send_create_user_request(base_url, new_user):
    print("Iniciando requisição ...")
    response = requests.post(f"{base_url}/usuarios", json=new_user)
    return response

def validate_user_creation(response):
    print("Validando statuscode ...")
    if response.status_code == 201:
        created_user = response.json()
        print("Usuário criado com sucesso")
        assert created_user["message"] == "Cadastro realizado com sucesso"
    else:
        print(f"Erro ao criar usuário: Status code {response.status_code}")
        print(f"Resposta: {response.text}")
        # Você pode lançar uma exceção ou lidar com o erro de outra forma
        raise Exception(f"Falha na criação do usuário. Status code: {response.status_code}")