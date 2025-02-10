import requests

url = 'http://127.0.0.1:5000/prever'

# Dados para enviar
dados = {
    'comprimento_sepala': 5.1,
    'largura_sepala': 3.5,
    'comprimento_petala': 1.4,
    'largura_petala': 0.2
}

response = requests.post(url, json=dados)

# Verificar a resposta
print(response.json())
