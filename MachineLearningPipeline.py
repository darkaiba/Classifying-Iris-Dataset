import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# Carregar o conjunto de dados
iris = load_iris()
X = iris.data  # Características (comprimento e largura da sépala e pétala)
y = iris.target  # Labels (classes)

# Dividir em dados de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Normalização dos dados
    ('svc', SVC(kernel='linear', random_state=42))  # Classificador SVM
])

# Treinar o modelo
pipeline.fit(X_train, y_train)

# Avaliar o modelo
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy * 100:.2f}%')

# Salvar o modelo treinado
joblib.dump(pipeline, 'modelo_iris.pkl')
