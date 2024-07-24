# Projeto de Automação de Testes de API REST com Python

Este é um exemplo básico de um projeto de automação de testes de API REST usando Python, `requests` e `pytest`.

## Estrutura do Projeto

- `tests/`: Contém os arquivos de testes.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.

## Como Executar

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Execute os testes:
    ```bash
    pytest
    ```

# def test_get_users(base_url):
#     response = requests.get(f"{base_url}/users")
#     assert response.status_code == 200
#     assert len(response.json()) > 0

# def test_get_user_by_id(base_url):
#     user_id = 1
#     response = requests.get(f"{base_url}/users/{user_id}")
#     assert response.status_code == 200
#     user = response.json()
#     assert user["id"] == user_id
#     assert "name" in user
#     assert "email" in user

# def test_create_user(base_url):
#     new_user = {
#         "name": "John Doe",
#         "username": "johndoe",
#         "email": "johndoe@example.com"
#     }
#     response = requests.post(f"{base_url}/users", json=new_user)
#     assert response.status_code == 201
#     created_user = response.json()
#     assert created_user["name"] == new_user["name"]
#     assert created_user["username"] == new_user["username"]
#     assert created_user["email"] == new_user["email"]