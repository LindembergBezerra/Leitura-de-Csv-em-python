import requests

# URL do arquivo CSV
csv_url = "https://raw.githubusercontent.com/digitalinnovationone/santander-dev-week-2023-api/main/SDW2023.csv"

# Nome do arquivo local
file_name = "SDW2023.csv"

# Baixar o arquivo
response = requests.get(csv_url)
if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"Arquivo '{file_name}' baixado com sucesso.")
else:
    print(
        f"Falha ao baixar o arquivo. Código de status: {response.status_code}")
    [
        {
            "id": 4,
            "name": "Pyterson",
            "account": {
                "id": 7,
                "number": "00001-1",
                "agency": "0001",
                "balance": 0.0,
                "limit": 500.0
            },
            "card": {
                "id": 4,
                "number": "**** **** **** 1111",
                "limit": 1000.0
            },
            "features": [],
            "news": [
                {
                    "id": 9,
                    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
                    "description": "Pyterson, invista hoje para garantir um futuro seguro e pr\u00f3spero. Seu futuro agradece!"
                }
            ]
        },
        {
            "id": 5,
            "name": "Pip",
            "account": {
                "id": 8,
                "number": "00002-2",
                "agency": "0001",
                "balance": 0.0,
                "limit": 500.0
            },
            "card": {
                "id": 5,
                "number": "**** **** **** 2222",
                "limit": 1000.0
            },
            "features": [],
            "news": [
                {
                    "id": 10,
                    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
                    "description": "Invista hoje para um futuro seguro e est\u00e1vel, Pip. O seu futuro financeiro depende disso!"
                }
            ]
        },
        {
            "id": 6,
            "name": "Pep",
            "account": {
                "id": 9,
                "number": "00003-3",
                "agency": "0001",
                "balance": 0.0,
                "limit": 500.0
            },
            "card": {
                "id": 6,
                "number": "**** **** **** 3333",
                "limit": 1000.0
            },
            "features": [],
            "news": [
                {
                    "id": 11,
                    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
                    "description": "Oi Pep, investir \u00e9 a chave para multiplicar seu dinheiro. N\u00e3o deixe sua grana parada!"
                }
            ]
        }
    ]
