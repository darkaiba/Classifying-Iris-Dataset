from flask import Flask, request, jsonify
import joblib
import numpy as np

# Carregar o modelo treinado
model = joblib.load('modelo_iris.pkl')

app = Flask(__name__)


@app.route('/prever', methods=['POST'])
def prever():
    try:
        # Receber os dados da requisição
        dados = request.get_json()

        # Extrair as características (valores enviados na requisição)
        comprimento_sepala = dados['comprimento_sepala']
        largura_sepala = dados['largura_sepala']
        comprimento_petala = dados['comprimento_petala']
        largura_petala = dados['largura_petala']

        # Organizar os dados em um vetor numpy
        features = np.array([[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]])

        # Realizar a previsão
        previsao = model.predict(features)

        # Mapear a classe prevista de volta para o nome da espécie
        classes = ['Iris setosa', 'Iris versicolor', 'Iris virginica']
        resultado = classes[previsao[0]]

        # Retornar o resultado da previsão
        return jsonify({'espécie': resultado}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
    