import requests

# URL da rota da API
url = "http://127.0.0.1:5000/"

while True:
    texto = input("Digite um texto (ou 'sair' para sair): ")

    if texto.lower() == 'sair':
        break

    # Faça uma solicitação GET para a API para exibir uma mensagem de exemplo
    response = requests.get(url)

    if response.status_code == 200:
        mensagem = response.json().get("mensagem")
        print(mensagem)

    # Dados para a solicitação POST
    data = {
        "texto": texto
    }

    # Faça a solicitação POST para a API
    response = requests.post(url, json=data)

    # Verifique a resposta
    if response.status_code == 200:
        resultado = response.json()
        texto_censurado = resultado.get("texto_censurado")
        print(f"Texto censurado: {texto_censurado}")
    else:
        print("Erro na solicitação:")
        print(response.text)
