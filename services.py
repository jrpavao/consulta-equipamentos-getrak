import requests

def get_token():
    url = "https://api.getrak.com/newkoauth/oauth/token"
    headers = {
        "Authorization": "Basic ZXJwYXN0cmFuc2F0XzY5OlhLNnNzSC90Y1FuJDVQWUs=",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def get_equipamentos(token, ativo="Y"):
    url = "https://api.getrak.com/v0.2/equipamentos/integracao"
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "insomnia/8.6.1"
    }

    offset = 0
    limit = 100
    todos = []

    while True:
        params = {
            "sistema": "astransat",
            "ativo": ativo,
            "limit": limit,
            "offset": offset
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        page = response.json()
        if not page:
            break
        todos.extend(page)
        offset += limit

    return todos
