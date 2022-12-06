# Parametros vs Hiperparametros

Breve explicação da diferença entre Parâmetros e Hiperparâmetros


Ensemble → Por que apenas um modelo se podemos utilizar um grupo de modelos?

Estratégias:

- tirar a media das decisões (**bagging)**
- atribuir pesos a saída de cada estimador **(boosting)**
- faz uma votação entre os modelos e elege aquele que tiver melhor performance **(voting)**

Estas abordagens carregam um fator complicador que são os parâmetros que terão que ser ajustados/definidos 

Existem diversas estratégias de otimização de hiperparametros 

→ Mas qual e a diferença entre os parâmetros e os hiperparametros?

⇒ Os algoritmos de machine learning nada mais são que funções em Python, e estas funções carregam consigo parâmetros. Os parâmetros destes algoritmos de machine learning também podem ser denominados como hiperparametros

⇒ Quando treinamos um modelo de machine learning o resultado são números que denominamos como coeficientes do modelo, alguns gostam de chamar eles de parâmetros, estes parâmetros alimentam a função (o que podemos chamar de hiperparametros)

Todo modelo de Machine Learning possui parâmetros que permitem a customização do modelo. Esses parâmetros também são chamados de hiperparâmetros.

Em programação os algoritmos de Machine Learning são representados por funções e cada função possui os parâmetros de customização, exatamente o que chamamos de hiperparâmetros.

É comum ainda que as pessoas se refiram aos coeficientes do modelo (encontrados ao final do treinamento) como parâmetros.

Parte do nosso trabalho como Cientistas de Dados é encontrar a melhor combinação de hiperparâmetros para cada modelo.

Em Métodos Ensemble esse trabalho é ainda mais complexo, pois temos os hiperparâmetros do estimador base e os hiperparâmetros do modelo ensemble, conforme este exemplo abaixo:


- Estimador base:

estim_base = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=None, n_neighbors=5, p=2, weights='uniform')


- Modelo Ensemble:

BaggingClassifier(base_estimator=estim_base, bootstrap=True, bootstrap_features=False, max_features=0.5, max_samples=0.5, n_estimators=10, n_jobs=None, oob_score=False, random_state=None, verbose=0, warm_start=False)

