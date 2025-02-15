Classificando Conjunto de Dados Iris

Foi construido um modelo de machine learning que é capaz de classificar as flores utilizando a base de dados Íris,  em uma das três espécies (Iris setosa, Iris versicolor e Iris virginica) com base nas características de comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala. 

O conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta de íris. Foi criado uma pipeline escrita em Python para treinamento e avaliação do modelo

Em seguida, também foi desenvolvido uma API em Python que utiliza o modelo treinado. A API recebe 4 parâmetros:
    1. comprimento da sépala
    2. largura da sépala
    3. comprimento da pétala
    4. largura da pétala

A API realiza o processo de feature engineering e retornar o resultado da previsão.