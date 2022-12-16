# Demonstracao do algoritmo de aprendizado nao-supervisionado K-Means


Essencialmente o que faz o K-means é calcular a distância entre os pontos de dados. Definimos um dos pontos de dados como centroide para cada cluster (inicialmente escolhemos um dos pontos de dados de forma aleatória) e vamos calculando a distância Euclidiana de cada ponto de dado para o centroide e assim criando grupos (ou clusters) com pontos de dados que contenham distâncias similares para o centroide. O centroide pode mudar à medida que vamos calculando as similaridades. Com isso, o algoritmo é capaz de agrupar os dados por similaridade. E isso funciona muito bem na maioria dos casos.

Já encontramos a solução para um dos problemas e usaremos o K-means para o agrupamento e segmentação de clientes. Mas agora temos outro problema (isso é o que nós fazemos: usamos ciência para resolver problemas).

Vamos trabalhar com K = 3 para encontrar 3 segmentos de clientes. Poderíamos trabalhar com 4, 5 ou mesmo 10 clusters. Usar 1 ou 2 não faria muito sentido!

Mas temos (ou podemos ter) diversas variáveis de entrada, certo? Isso significa que temos dados com alta dimensionalidade. Se quisermos apresentar graficamente o resultado do agrupamento para os tomadores de decisão que não possuem conhecimento técnico em Machine Learning (e nem precisam ter), como faríamos isso? Um gráfico de 4 ou 5 dimensões é incompreensível e ainda ter que representar os clusters, deixaria tudo muito mais complicado.

E se reduzíssemos a dimensionalidade dos dados para que pudéssemos criar um gráfico de duas dimensões independente da quantidade de variáveis em nosso dataset? Lindo, não? Podemos usar PCA (Análise de Componentes Principais), uma das principais técnicas para redução de dimensionalidade. Perfeito. Mais um problema resolvido.

Tem outro problema. Para desenvolver o PCA a partir do zero também temos que montar toda a estrutura matemática por trás do PCA, o que implica calcular as matrizes de co-variância e correlação, a fim de encontrar autovalores e autovetores.


