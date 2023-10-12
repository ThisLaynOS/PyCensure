
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de palavras inadequadas
with open("config.json", "r") as arquivo:
    config = json.load(arquivo)
    palavroes = config["xingamentos"]

@app.route('/', methods=['POST'])
def censure():
    # Recebe o texto da solicitação
    data = request.get_json()
    texto = data.get('texto', '')
    for palavra in palavroes:
        texto = texto.replace(palavra, '*' * len(palavra))
    return jsonify({texto})

if __name__ == '__main__':
    app.run()




