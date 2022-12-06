# Recommendation system for Netflix movies


For all e-commerce businesses, it is likely that the recommendation are the most important analytical tool ever implemented. Although there is not official estimates, many sources estimate that, for the main platforms of e-commerce, such as Amazon and Netflix, recommendation systems can be responsible for up to 10% to 35% of the revenue of these companies. Those are considerable numbers. In a world with low growth, being able to increase your revenue by 10% makes
recommendation systems something we should look at more closely. Let's understand the these systems work.


Whenever we talk about some technology that can bring financial benefits to the company, which are significant, the investments in this technology are justified. And then we see an advantage of recommender systems (or perhaps one more). the cost of implementation of these systems is relatively low and their gains are substantial. Recommender systems are just one of many rapidly evolving specialties within predictive analytics and guaranteed work for Data Scientists.



## What Are Recommender Systems?

These are the applications that personalize the customer's shopping experience, recommending the next best options in light of your recent purchases or browsing activity.

Recommender Systems are, therefore, predictive models that, based on statistic, determine the probability that a customer will be interested in another item similar to what you are buying at any given time.

Recommender systems are simple, at least, in their objective.

But it is important to make it clear that while recommender systems are used in e-commerce applications where the customer is buying something, they are equally applicable in situations where you are trying to maximize user time on a website in order to increase advertising exposure. A good example is the Yahoo portal
that customizes your news feed so you spend more time on the site. This is a good example of application of recommender systems. You don't know (or at least you don't
knew until now), but the news that are being recommended to you on the portal aim to increase your exposure to the site's advertisers, who pay for exactly the number of views or clicks on your banners. Other examples of recommendation systems include associations and Market Basket Analysis which are so useful for activities of marketing.

# Filtragem de Conteudo

Filtragem baseada em conteúdo foi o estado da arte há 10 anos e ainda é bastante encontrado em uso e tem muitas aplicações na atualidade, mas com o crescimento exponencial o volume de dados, esta técnica perdeu espaço para os filtros colaborativos e você já vai entender o porquê.

Como o nome indica, a filtragem de conteúdo procura semelhanças entre os itens que o cliente consumiu ou navegou no passado para apresentar opções no futuro. Filtragem de onteúdo são classificadores específicos que aprendem a categorizar positivamente ou negativamente as alternativas baseadas nos gostos ou desagrados do usuário. E quando alamos de conteúdo estamos nos referindo aos atributos dos itens que estão sendo recomendados. Por exemplo, um serviço de músicas online como o Spotify, pode apresentar m sistema de recomendação baseado em conteúdo considerando os atributos das músicas como autor, gênero, ano) e também o perfil do usuário.

Na filtragem colaborativa, consideramos apenas as preferências de itens do usuário e riamos os sistemas de recomendação. Embora essa abordagem seja precisa, faz mais sentido e considerarmos as propriedades do usuário e as propriedades do item enquanto construímos otores de recomendação. Ao contrário da filtragem colaborativa, usamos as propriedades do tem e as preferências do usuário nas propriedades do item enquanto criamos mecanismos de
recomendação baseados em conteúdo. Um sistema de recomendação de conteúdo normalmente contém uma etapa de geração de perfil de usuário, etapa de geração de perfil de
item e criação de modelo para gerar recomendações para um usuário ativo. O sistema de recomendação baseado em conteúdo recomenda itens aos usuários, levando em consideração o conteúdo ou atributos de itens e perfis de usuário. Como exemplo, se você pesquisou vídeos de Lionel Messi no YouTube, o sistema de recomendação baseado em conteúdo aprenderá suas preferências e recomendará outros vídeos relacionados a Lionel Messi e outros vídeos
relacionados ao futebol.

Em termos mais simples, o sistema recomenda itens semelhantes aos que o usuário gostou no passado. A similaridade de itens é calculada com base nos atributos associados aos outros itens comparados e é combinada com as preferências históricas do usuário. Ao construir um sistema de recomendação baseado em conteúdo, levamos em consideração as seguintes perguntas: Como escolhemos conteúdo ou recursos dos produtos? Como criamos perfis de usuário com preferências semelhantes às do conteúdo do produto? Como criar semelhança entre itens com base em suas características? Como criar e atualizar perfis de usuário continuamente?

Mas afinal, qual a diferença deste tipo de sistema de recomendação, para os filtros colaborativos? Essa técnica não leva em consideração as preferências de vizinhança do usuário. Portanto, não exige uma grande preferência do grupo de usuários por itens para uma melhor precisão de recomendação. Considera apenas as preferências passadas do usuário e as propriedades / características dos itens.

O sistema cria um perfil baseado em conteúdo específico do usuário usando atributos discretos. O histórico de consumo ou navegação do usuário é usado para criar um vetor ponderado dos atributos do item. Os pesos são aprendidos ou atribuídos para variar a importância dos atributos para o usuário em particular. Esse peso é usado para comparar com o peso do vetor de diferentes itens que podem ser recomendados. As técnicas de cálculo podem variar de médias simples ponderadas a classificadores bayesianos, análise de agrupamentos, árvores de decisão ou abordagens mais complexas, incluindo redes neurais artificiais.
Um requisito é que você seja capaz de fornecer um número razoavelmente grande de descritores de conteúdo para usar na classificação. Estes podem ser booleanos (o filme é animado, sim ou não, por exemplo). Eles também podem ser contínuos, como a classificação recebida pelo filme a partir de uma fonte de classificação, a "classificação média por estrelas" de outros clientes que consumiram o item ou a porcentagem ou o número de minutos no filme considerado "ação" ou 'romance'. A capacidade de adquirir e manter atributos de conteúdo é um critério chave e uma limitação fundamental deste tipo de sistema de recomendação. Alguns atributos podem ser fáceis de adquirir, mas outros não (por exemplo, atributos constantemente atualizados de produtos eletrônicos ou atributos de filmes). Em ambientes como filmes, música e notícias, o inventário pode mudar tão rapidamente e ser tão grande que adquirir e manter atributos é muito difícil ou muito caro. O site de recomendação de filmes Rotten Tomatoes e o site de Radio na Internet, o Pandora, são exemplos de sistemas de recomendação baseados em conteúdo.

# Filtros Colaborativos

A filtragem colaborativa foca o usuário e outros usuários que são matematicamente similares. Em teoria, não são necessários atributos específicos para o conteúdo que os filtros colaborativos podem inferir. Mais tarde veremos que adicionar atributos de conteúdo pode melhorar o desempenho, mas não é tecnicamente necessário. A premissa é que se dois usuários tiveram uma forte semelhança de gostos e desgostos no passado, é provável que eles vão continuar a ter uma forte semelhança no futuro. Sistemas de recomendação baseados em Filtros Colaborativos irão recomendar às pessoas que gostam de filmes de romance, aqueles filmes que têm forte conteúdo romântico sem a exigência de definir necessariamente o que seja "romance". São apenas números sendo analisados. Uma vez estabelecida a semelhança, os itens consumidos por um usuário podem ser recomendados a outros usuários semelhantes. Essa é a ideia por trás dos filtros colaborativos.

![image](https://user-images.githubusercontent.com/79231882/206012435-081d7aba-997e-4c2c-be90-f3586b59a6d5.png)

Sistemas de recomendação de filtragem colaborativa são formas básicas de motores de recomendação. Neste tipo de mecanismo de recomendação, filtrar itens de um grande
conjunto de alternativas é feito pela colaboração de preferências dos usuários. A suposição básica em um sistema de recomendação de filtragem colaborativa é que, se dois usuários compartilharam os mesmos interesses um do outro no passado, eles também terão gostos semelhantes no futuro. Se, por exemplo, o usuário A e o usuário B tiverem preferências de filme semelhantes, e o usuário A assistiu recentemente ao Titanic, que o usuário B ainda não viu, então a ideia é recomendar esse filme ao usuário B. As recomendações do filme no Netflix são um bom exemplo deste tipo de sistema de recomendação. Existem dois subtipos de sistemas de recomendação de filtragem colaborativa:

![image](https://user-images.githubusercontent.com/79231882/206012584-fc99a608-3408-4916-967e-8023c1a75574.png)

Na filtragem colaborativa baseada no usuário (User Based), as recomendações são geradas considerando as preferências na vizinhança do usuário. A filtragem colaborativa
baseada em usuário é feita em duas etapas: Identificar usuários semelhantes com base em preferências de outros usuários semelhantes e recomendar novos itens a um usuário ativo com base na classificação dada por usuários semelhantes.

Nos sistemas baseados em itens (Item Based), as recomendações podem ser feitas com base na semelhança de produtos com outros produtos que o cliente comprou ou navegou.

A vantagem dos sistemas de filtragem colaborativa é que eles são simples de implementar e muito precisos. No entanto, eles têm seu próprio conjunto de limitações, como o problema do Cold Start (ou início frio), o que significa que os sistemas de filtragem colaborativa falham em recomendar aos usuários iniciantes cujas informações não estão disponíveis no sistema.

Ao construir sistemas de recomendação de filtragem colaborativa, vamos aprender sobre os seguintes aspectos: Como calcular a similaridade entre os usuários? Como calcular a similaridade entre itens? Como são geradas as recomendações? Como lidar com novos itens e novos usuários cujos dados não são conhecidos?


# Modelos Hibridos

Os motores de recomendação híbridos são construídos pela combinação de vários sistemas de recomendação para construir um sistema mais robusto. Ao combinar vários
sistemas de recomendação, podemos substituir as desvantagens de um sistema com as vantagens de outro sistema e, assim, construir um sistema final mais confiável. Por exemplo, ao combinar métodos de filtragem colaborativa (em que o modelo falha quando novos itens não possuem classificação), com sistemas baseados em conteúdo (onde informações de atributos sobre os itens estão disponíveis), novos produtos podem ser recomendados com mais precisão e eficiência.

Por exemplo, se você é um leitor frequente de notícias no Google News, o mecanismo de recomendação, recomenda artigos de notícias para você, combinando artigos de notícias populares, lidos por pessoas semelhantes a você e usando suas preferências pessoais, calculadas usando as informações do clique anterior. Com este tipo de sistema de recomendação, as recomendações de filtragem colaborativa são combinadas com recomendações baseadas em conteúdo para gerar as recomendações finais.

Antes de construir um modelo híbrido, devemos considerar as seguintes perguntas: Que técnicas de recomendação devem ser combinadas para alcançar a solução de negócios? Como combinar várias técnicas e seus resultados para melhores previsões? A vantagem dos motores de recomendação híbridos é que esta abordagem irá aumentar a eficiência das recomendações em comparação com as técnicas de recomendação individuais. Esta abordagem também sugere uma boa mistura de recomendações para os usuários, tanto no nível personalizado quanto no nível de usuários similares.

Não existem práticas universais específicas para sistemas de recomendação híbridos, e sua construção exigirá a sua visão (você Cientista de Dados) sobre as circunstâncias especiais do problema de negócio a ser resolvido.


# O que sao sistemas de recomendacao?

Para todos os negócios ligados a comércio eletrônico, é provável que os sistemas de recomendação sejam a ferramenta analítica mais importante já implementada. Embora não existam estimativas oficiais, muitas fontes estimam que, para as principais plataformas de comércio eletrônico, como a Amazon e a Netflix, os sistemas de recomendação podem ser responsáveis por até 10% a 35% da receita destas empresas. Esses são números consideráveis. Em um mundo com baixo crescimento, conseguir aumentar em 10% o seu faturamento, faz dos sistemas de recomendação algo que devemos olhar com mais atenção. Vamos compreender o que são esses sistemas.

Sempre que falamos em alguma tecnologia que pode trazer benefícios financeiros para a empresa, que sejam significativos, os investimentos nesta tecnologia se justificam. E aí vemos uma vantagem dos sistemas de recomendação (ou talvez mais uma). O custo de implementação desses sistemas é relativamente baixo e seus ganhos são consideráveis. Sistemas de recomendação são apenas uma das muitas especialidades em rápida evolução dentro de análise preditiva e trabalho garantido para os Cientistas de Dados.


## O Que São Sistemas de Recomendação?

São as aplicações que personalizam a experiência de compra do cliente, recomendando as melhores opções seguintes à luz das suas recentes compras ou atividade de navegação.

Sistemas de Recomendação são, portanto, modelos preditivos que a partir de análise estatística, determinam a probabilidade de um cliente estar interessado por um outro item similar ao que está comprando em um dado momento.

Sistemas de recomendação são simples, pelo menos, em seu objetivo.

Mas é importante deixar claro, que enquanto sistemas de recomendação são usados em aplicativos de comércio eletrônico onde o cliente está comprando algo, eles são igualmente aplicáveis em situações em que você está tentando maximizar o tempo do usuário em um site com a finalidade de aumentar a exposição publicitária. Um bom exemplo é o portal do Yahoo que personaliza seu feed de notícias de modo que você gaste mais tempo no site. Este é um bom exemplo de aplicação de sistemas de recomendação. Você não sabe (ou pelo menos não sabia até agora), mas as notícias que vão sendo recomendadas a você no portal têm como objetivo aumentar sua exposição aos anunciantes do site, que pagam exatamente pelo número de visualizações ou de cliques em seus banners. Outros exemplos de sistemas de recomendação incluem associações e Market Basket Analysis que são tão úteis para atividades de Marketing.


# Associação e Modelos Market Basket

Sistemas de recomendação baseados em análise de Associação e Análise de Cesta de Mercado (Market Basket) olham quase exclusivamente em conteúdo. Este tipo de análise
estatística baseia-se apenas no mais simples dos cálculos para encontrar itens que são frequentemente consumidos juntos. A análise matemática de associação e de market basket é a mesma. Quando os clientes normalmente adquirem os itens ou serviços um de cada vez (como serviços bancários) chamamos de Associação. Quando os clientes potencialmente compram várias coisas de uma só vez chamamos de Market Basket. Assim, a Análise da Associação é realizada ao nível do cliente, enquanto a Análise de Market Basket é conduzida ao nível da transação. Existem três etapas principais neste processo de análise:

  1. Avaliar a força da relação entre cada um de seus produtos e todos os outros produtos que você oferece usando os algoritmos de associação.
  2. Identificar aqueles pares que têm afinidade muito forte (tipicamente uma pontuação de afinidade de 2 ou superior). Por exemplo, um cliente com um cartão de crédito pode ter duas ou três vezes mais probabilidade de adquirir um empréstimo do que um cliente selecionado ao acaso.
  3. Criar uma oferta personalizada para clientes que têm um produto (de um par de produtos fortemente associados), mas não o outro. 
  
Vantagens:

  • É extremamente simples e rápido.
  • Funcionará com bases de clientes muito pequenas.
  • O conhecimento do cliente e seu relacionamento com produtos e serviços não é necessário.
  • A preparação de dados é mínima.
  • Associação e Market Basket Analysis são normalmente o método mais rentável para criar ofertas personalizadas.


# Evolução dos Sistemas de Recomendação

Ao longo dos anos, os sistemas de recomendação evoluíram, passaram de métodos mais básicos baseados em similaridades para sistemas de recomendações personalizadas, de
recomendações baseadas em contexto, para recomendações em tempo real, de recomendações baseadas em heurísticas básicas, como cálculo de similaridade para abordagens baseadas em Machine Learning.

Nos estágios iniciais desses sistemas de recomendação, apenas as classificações dos usuários sobre os produtos foram utilizadas para gerar recomendações. Nessa época, os pesquisadores usavam apenas as informações de classificação disponíveis. Eles simplesmente aplicaram abordagens heurísticas como o cálculo de similaridade usando distâncias euclidianas, o coeficiente de Pearson, similaridade de cosseno e etc…. Essas abordagens foram bem recebidas e, surpreendentemente, elas funcionam muito bem até hoje.

Esta primeira geração de motores de recomendação é chamada de filtragem colaborativa ou sistemas de recomendação de métodos de vizinhança. Embora eles executem muito bem, estes sistemas vêm com seu próprio conjunto de limitações, tais como problemas de Cold Start (Início frio), quando não são capazes de recomendar produtos a novos usuários sem informações de classificação. Além disso, esses sistemas não conseguem lidar com cenários onde os dados são muito escassos, de modo que as classificações de usuários dos produtos são muito menores.

Para superar essas limitações, novas abordagens foram desenvolvidas. Por exemplo, a fim de lidar com problemas de conjuntos de dados muito esparsos, abordagens matemáticas, como Fatoração de Matriz e Singular Value Decompositions, têm sido utilizados. São técnicas matemáticas que ajudam a resolver problemas nos dados, aumentando a eficácia de sistemas de recomendação.

No início, os cálculos de similaridade foram usados em sistemas de recomendação baseados em conteúdo, mas com avanços em tecnologia e infraestrutura, métodos mais
avançados, como modelos de aprendizado de máquina, substituíram os métodos heurísticos. Estes novos modelos baseados em Machine Learning melhoraram a precisão das
recomendações. Embora os sistemas de recomendação baseados em conteúdo tenham resolvido muitas das deficiências da filtragem colaborativa, eles têm suas próprias deficiências inerentes, como não ser capaz de recomendar novos itens fora do escopo de preferência do usuário, o que a filtragem colaborativa poderia fazer.

Para resolver esse problema, os pesquisadores começaram a combinar diferentes modelos de recomendação para chegar a modelos híbridos, que são muito mais poderosos do que qualquer um dos modelos individuais. E esses modelos híbridos atualmente englobam não apenas os modelos tradicionais de sistemas de recomendação, como técnicas matemáticas e de Machine Learning, levando a sistemas totalmente personalizados a cada cliente.

Com implementações bem-sucedidas de mecanismos de recomendação personalizados, as pessoas começaram a estender a personalização a outras dimensões chamadas contextos,
como a adição de localização, hora, grupo e assim por diante e alteraram o conjunto de recomendações com cada contexto. Com avanços em tecnologia como grandes ecossistemas de dados, ferramentas analíticas que executam em memória e em tempo real como o Apache Spark, a capacidade de manipulação de bancos de dados muito grandes tornou-se possível. Atualmente estamos nos movendo para sistemas ainda mais personalizados com o uso de inteligência artificial. No aspecto de tecnologia, as recomendações estão passando de abordagens de aprendizado de máquina para abordagens mais avançadas de aprendizagem profunda como redes neurais.


# Sistema de Recomendação Baseado no Item Mais Popular

Este é o modelo mais simples e básico de sistema de recomendação.

A estratégia é simplesmente oferecer ao cliente o que é mais popular, seja um filme, um livro ou um artigo de vestuário. Sem fazer nada mais do que observar nos registros de vendas, é possível construir um sistema de recomendação simples como esse. Isso não é necessariamente ciência de dados. Não é particularmente personalizado. Mas pode ser útil se você sabe muito pouco sobre o seu visitante.

Exige alguns atributos de conteúdos que podem ser usados para criar subcategorias que podem corresponder à navegação atual do visitante em um site de comércio eletrônico. Por exemplo, se você está oferecendo uma grande variedade de produtos como um único pacote ou combo, desde ferramentas a roupas, ou filmes, livros ou notícias que apelam para interesses diferentes, então você precisará tentar combinar itens pelo menos na mesma categoria visualizada pelo seu visitante. Empresas como a rede de lojas Home Depot usa regularmente um espaço em seu website chamado de "best sellers" e a GAP usa regularmente "produtos mais recentes" para indicar os produtos mais populares, indicá-los a outros consumidores e aumentar a receita. Esse tipo de sistema de recomendação pode ser usado como uma estratégia complementar a outros sistemas mais robustos.

![image](https://user-images.githubusercontent.com/79231882/206015500-27d5c773-0b03-4398-aaef-592eb09ceb04.png)


# Tipos de Sistemas de Recomendação

Sistemas de recomendação não são todos iguais. Se você for implementar um sistema de recomendação pela primeira vez é muito provável que você comece com uma solução
pronta de um fornecedor ou que você desenvolva seu próprio sistema do zero usando R ou Python por exemplo e faremos isso daqui a pouco. Além das questões táticas de negócios sobre as considerações que devem ser feitas na implementação de sistemas de recomendação, é importante conhecer tecnicamente o que são esses sistemas. Isso significa olhar profundamente para os diferentes tipos de sistema de recomendação e compreender os pontos fortes e fracos de cada um.

Os tipos de sistemas de recomendação dependem de diferentes algoritmos.

  • Alguns têm um foco maior nas semelhanças de clientes, alguns em similaridades de conteúdo e alguns uma mistura dos dois.

  • Diferentes algoritmos variam em sua utilidade com base no quanto você sabe com antecedência sobre os clientes, seu conteúdo e se você pode obter feedback dos clientes após a compra (isso seria fundamental).

  • Todos devem satisfazer a exigência geral de oferecer um resultado personalizado dentro de cerca de 50 milissegundos (esse é um desafio).

Os sistemas de recomendação se resumem a oferecer pontuações aos clientes de acordo com vários critérios. Essas tags de pontuação que você coloca nos clientes e registros de conteúdo raramente são em tempo real e são normalmente atualizadas durante a noite, mais ou menos frequentemente, dependendo de cada circunstância e objetivo de negócio. Portanto, as atualizações de pontuação off-line podem depender de cálculos recomendados, mas podem ser complementadas com pontuação e análise realizadas separadamente em uma escala de tempo mais longa. Ou seja, o que parece tempo real é na verdade quase tempo real.

![image](https://user-images.githubusercontent.com/79231882/206015872-b31afce6-6cec-4a17-a454-2e381f08d4f1.png)

Os avanços nos sistemas de recomendação não foram tão grandes quanto algumas outras áreas da ciência de dados. A mais complexa dessas opções, os Filtros Colaborativos, existem a mais de dez anos. De uma perspectiva empresarial a boa notícia é que você pode se sentir confortável construindo um portfólio de tecnologia existente e bem estabelecida. A maioria dos avanços na ciência dos dados em torno de sistemas de recomendação tem sido focada em melhorar gradualmente o seu desempenho nos domínios específicos em que foram implantados. E com a grande quantidade de dados disponíveis (Big Data), desempenho deve ser uma preocupação constante.
