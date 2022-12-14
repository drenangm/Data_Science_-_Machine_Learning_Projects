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

Filtragem baseada em conte??do foi o estado da arte h?? 10 anos e ainda ?? bastante encontrado em uso e tem muitas aplica????es na atualidade, mas com o crescimento exponencial o volume de dados, esta t??cnica perdeu espa??o para os filtros colaborativos e voc?? j?? vai entender o porqu??.

Como o nome indica, a filtragem de conte??do procura semelhan??as entre os itens que o cliente consumiu ou navegou no passado para apresentar op????es no futuro. Filtragem de onte??do s??o classificadores espec??ficos que aprendem a categorizar positivamente ou negativamente as alternativas baseadas nos gostos ou desagrados do usu??rio. E quando alamos de conte??do estamos nos referindo aos atributos dos itens que est??o sendo recomendados. Por exemplo, um servi??o de m??sicas online como o Spotify, pode apresentar m sistema de recomenda????o baseado em conte??do considerando os atributos das m??sicas como autor, g??nero, ano) e tamb??m o perfil do usu??rio.

Na filtragem colaborativa, consideramos apenas as prefer??ncias de itens do usu??rio e riamos os sistemas de recomenda????o. Embora essa abordagem seja precisa, faz mais sentido e considerarmos as propriedades do usu??rio e as propriedades do item enquanto constru??mos otores de recomenda????o. Ao contr??rio da filtragem colaborativa, usamos as propriedades do tem e as prefer??ncias do usu??rio nas propriedades do item enquanto criamos mecanismos de
recomenda????o baseados em conte??do. Um sistema de recomenda????o de conte??do normalmente cont??m uma etapa de gera????o de perfil de usu??rio, etapa de gera????o de perfil de
item e cria????o de modelo para gerar recomenda????es para um usu??rio ativo. O sistema de recomenda????o baseado em conte??do recomenda itens aos usu??rios, levando em considera????o o conte??do ou atributos de itens e perfis de usu??rio. Como exemplo, se voc?? pesquisou v??deos de Lionel Messi no YouTube, o sistema de recomenda????o baseado em conte??do aprender?? suas prefer??ncias e recomendar?? outros v??deos relacionados a Lionel Messi e outros v??deos
relacionados ao futebol.

Em termos mais simples, o sistema recomenda itens semelhantes aos que o usu??rio gostou no passado. A similaridade de itens ?? calculada com base nos atributos associados aos outros itens comparados e ?? combinada com as prefer??ncias hist??ricas do usu??rio. Ao construir um sistema de recomenda????o baseado em conte??do, levamos em considera????o as seguintes perguntas: Como escolhemos conte??do ou recursos dos produtos? Como criamos perfis de usu??rio com prefer??ncias semelhantes ??s do conte??do do produto? Como criar semelhan??a entre itens com base em suas caracter??sticas? Como criar e atualizar perfis de usu??rio continuamente?

Mas afinal, qual a diferen??a deste tipo de sistema de recomenda????o, para os filtros colaborativos? Essa t??cnica n??o leva em considera????o as prefer??ncias de vizinhan??a do usu??rio. Portanto, n??o exige uma grande prefer??ncia do grupo de usu??rios por itens para uma melhor precis??o de recomenda????o. Considera apenas as prefer??ncias passadas do usu??rio e as propriedades / caracter??sticas dos itens.

O sistema cria um perfil baseado em conte??do espec??fico do usu??rio usando atributos discretos. O hist??rico de consumo ou navega????o do usu??rio ?? usado para criar um vetor ponderado dos atributos do item. Os pesos s??o aprendidos ou atribu??dos para variar a import??ncia dos atributos para o usu??rio em particular. Esse peso ?? usado para comparar com o peso do vetor de diferentes itens que podem ser recomendados. As t??cnicas de c??lculo podem variar de m??dias simples ponderadas a classificadores bayesianos, an??lise de agrupamentos, ??rvores de decis??o ou abordagens mais complexas, incluindo redes neurais artificiais.
Um requisito ?? que voc?? seja capaz de fornecer um n??mero razoavelmente grande de descritores de conte??do para usar na classifica????o. Estes podem ser booleanos (o filme ?? animado, sim ou n??o, por exemplo). Eles tamb??m podem ser cont??nuos, como a classifica????o recebida pelo filme a partir de uma fonte de classifica????o, a "classifica????o m??dia por estrelas" de outros clientes que consumiram o item ou a porcentagem ou o n??mero de minutos no filme considerado "a????o" ou 'romance'. A capacidade de adquirir e manter atributos de conte??do ?? um crit??rio chave e uma limita????o fundamental deste tipo de sistema de recomenda????o. Alguns atributos podem ser f??ceis de adquirir, mas outros n??o (por exemplo, atributos constantemente atualizados de produtos eletr??nicos ou atributos de filmes). Em ambientes como filmes, m??sica e not??cias, o invent??rio pode mudar t??o rapidamente e ser t??o grande que adquirir e manter atributos ?? muito dif??cil ou muito caro. O site de recomenda????o de filmes Rotten Tomatoes e o site de Radio na Internet, o Pandora, s??o exemplos de sistemas de recomenda????o baseados em conte??do.

# Filtros Colaborativos

A filtragem colaborativa foca o usu??rio e outros usu??rios que s??o matematicamente similares. Em teoria, n??o s??o necess??rios atributos espec??ficos para o conte??do que os filtros colaborativos podem inferir. Mais tarde veremos que adicionar atributos de conte??do pode melhorar o desempenho, mas n??o ?? tecnicamente necess??rio. A premissa ?? que se dois usu??rios tiveram uma forte semelhan??a de gostos e desgostos no passado, ?? prov??vel que eles v??o continuar a ter uma forte semelhan??a no futuro. Sistemas de recomenda????o baseados em Filtros Colaborativos ir??o recomendar ??s pessoas que gostam de filmes de romance, aqueles filmes que t??m forte conte??do rom??ntico sem a exig??ncia de definir necessariamente o que seja "romance". S??o apenas n??meros sendo analisados. Uma vez estabelecida a semelhan??a, os itens consumidos por um usu??rio podem ser recomendados a outros usu??rios semelhantes. Essa ?? a ideia por tr??s dos filtros colaborativos.

![image](https://user-images.githubusercontent.com/79231882/206012435-081d7aba-997e-4c2c-be90-f3586b59a6d5.png)

Sistemas de recomenda????o de filtragem colaborativa s??o formas b??sicas de motores de recomenda????o. Neste tipo de mecanismo de recomenda????o, filtrar itens de um grande
conjunto de alternativas ?? feito pela colabora????o de prefer??ncias dos usu??rios. A suposi????o b??sica em um sistema de recomenda????o de filtragem colaborativa ?? que, se dois usu??rios compartilharam os mesmos interesses um do outro no passado, eles tamb??m ter??o gostos semelhantes no futuro. Se, por exemplo, o usu??rio A e o usu??rio B tiverem prefer??ncias de filme semelhantes, e o usu??rio A assistiu recentemente ao Titanic, que o usu??rio B ainda n??o viu, ent??o a ideia ?? recomendar esse filme ao usu??rio B. As recomenda????es do filme no Netflix s??o um bom exemplo deste tipo de sistema de recomenda????o. Existem dois subtipos de sistemas de recomenda????o de filtragem colaborativa:

![image](https://user-images.githubusercontent.com/79231882/206012584-fc99a608-3408-4916-967e-8023c1a75574.png)

Na filtragem colaborativa baseada no usu??rio (User Based), as recomenda????es s??o geradas considerando as prefer??ncias na vizinhan??a do usu??rio. A filtragem colaborativa
baseada em usu??rio ?? feita em duas etapas: Identificar usu??rios semelhantes com base em prefer??ncias de outros usu??rios semelhantes e recomendar novos itens a um usu??rio ativo com base na classifica????o dada por usu??rios semelhantes.

Nos sistemas baseados em itens (Item Based), as recomenda????es podem ser feitas com base na semelhan??a de produtos com outros produtos que o cliente comprou ou navegou.

A vantagem dos sistemas de filtragem colaborativa ?? que eles s??o simples de implementar e muito precisos. No entanto, eles t??m seu pr??prio conjunto de limita????es, como o problema do Cold Start (ou in??cio frio), o que significa que os sistemas de filtragem colaborativa falham em recomendar aos usu??rios iniciantes cujas informa????es n??o est??o dispon??veis no sistema.

Ao construir sistemas de recomenda????o de filtragem colaborativa, vamos aprender sobre os seguintes aspectos: Como calcular a similaridade entre os usu??rios? Como calcular a similaridade entre itens? Como s??o geradas as recomenda????es? Como lidar com novos itens e novos usu??rios cujos dados n??o s??o conhecidos?


# Modelos Hibridos

Os motores de recomenda????o h??bridos s??o constru??dos pela combina????o de v??rios sistemas de recomenda????o para construir um sistema mais robusto. Ao combinar v??rios
sistemas de recomenda????o, podemos substituir as desvantagens de um sistema com as vantagens de outro sistema e, assim, construir um sistema final mais confi??vel. Por exemplo, ao combinar m??todos de filtragem colaborativa (em que o modelo falha quando novos itens n??o possuem classifica????o), com sistemas baseados em conte??do (onde informa????es de atributos sobre os itens est??o dispon??veis), novos produtos podem ser recomendados com mais precis??o e efici??ncia.

Por exemplo, se voc?? ?? um leitor frequente de not??cias no Google News, o mecanismo de recomenda????o, recomenda artigos de not??cias para voc??, combinando artigos de not??cias populares, lidos por pessoas semelhantes a voc?? e usando suas prefer??ncias pessoais, calculadas usando as informa????es do clique anterior. Com este tipo de sistema de recomenda????o, as recomenda????es de filtragem colaborativa s??o combinadas com recomenda????es baseadas em conte??do para gerar as recomenda????es finais.

Antes de construir um modelo h??brido, devemos considerar as seguintes perguntas: Que t??cnicas de recomenda????o devem ser combinadas para alcan??ar a solu????o de neg??cios? Como combinar v??rias t??cnicas e seus resultados para melhores previs??es? A vantagem dos motores de recomenda????o h??bridos ?? que esta abordagem ir?? aumentar a efici??ncia das recomenda????es em compara????o com as t??cnicas de recomenda????o individuais. Esta abordagem tamb??m sugere uma boa mistura de recomenda????es para os usu??rios, tanto no n??vel personalizado quanto no n??vel de usu??rios similares.

N??o existem pr??ticas universais espec??ficas para sistemas de recomenda????o h??bridos, e sua constru????o exigir?? a sua vis??o (voc?? Cientista de Dados) sobre as circunst??ncias especiais do problema de neg??cio a ser resolvido.


# O que sao sistemas de recomendacao?

Para todos os neg??cios ligados a com??rcio eletr??nico, ?? prov??vel que os sistemas de recomenda????o sejam a ferramenta anal??tica mais importante j?? implementada. Embora n??o existam estimativas oficiais, muitas fontes estimam que, para as principais plataformas de com??rcio eletr??nico, como a Amazon e a Netflix, os sistemas de recomenda????o podem ser respons??veis por at?? 10% a 35% da receita destas empresas. Esses s??o n??meros consider??veis. Em um mundo com baixo crescimento, conseguir aumentar em 10% o seu faturamento, faz dos sistemas de recomenda????o algo que devemos olhar com mais aten????o. Vamos compreender o que s??o esses sistemas.

Sempre que falamos em alguma tecnologia que pode trazer benef??cios financeiros para a empresa, que sejam significativos, os investimentos nesta tecnologia se justificam. E a?? vemos uma vantagem dos sistemas de recomenda????o (ou talvez mais uma). O custo de implementa????o desses sistemas ?? relativamente baixo e seus ganhos s??o consider??veis. Sistemas de recomenda????o s??o apenas uma das muitas especialidades em r??pida evolu????o dentro de an??lise preditiva e trabalho garantido para os Cientistas de Dados.


## O Que S??o Sistemas de Recomenda????o?

S??o as aplica????es que personalizam a experi??ncia de compra do cliente, recomendando as melhores op????es seguintes ?? luz das suas recentes compras ou atividade de navega????o.

Sistemas de Recomenda????o s??o, portanto, modelos preditivos que a partir de an??lise estat??stica, determinam a probabilidade de um cliente estar interessado por um outro item similar ao que est?? comprando em um dado momento.

Sistemas de recomenda????o s??o simples, pelo menos, em seu objetivo.

Mas ?? importante deixar claro, que enquanto sistemas de recomenda????o s??o usados em aplicativos de com??rcio eletr??nico onde o cliente est?? comprando algo, eles s??o igualmente aplic??veis em situa????es em que voc?? est?? tentando maximizar o tempo do usu??rio em um site com a finalidade de aumentar a exposi????o publicit??ria. Um bom exemplo ?? o portal do Yahoo que personaliza seu feed de not??cias de modo que voc?? gaste mais tempo no site. Este ?? um bom exemplo de aplica????o de sistemas de recomenda????o. Voc?? n??o sabe (ou pelo menos n??o sabia at?? agora), mas as not??cias que v??o sendo recomendadas a voc?? no portal t??m como objetivo aumentar sua exposi????o aos anunciantes do site, que pagam exatamente pelo n??mero de visualiza????es ou de cliques em seus banners. Outros exemplos de sistemas de recomenda????o incluem associa????es e Market Basket Analysis que s??o t??o ??teis para atividades de Marketing.


# Associa????o e Modelos Market Basket

Sistemas de recomenda????o baseados em an??lise de Associa????o e An??lise de Cesta de Mercado (Market Basket) olham quase exclusivamente em conte??do. Este tipo de an??lise
estat??stica baseia-se apenas no mais simples dos c??lculos para encontrar itens que s??o frequentemente consumidos juntos. A an??lise matem??tica de associa????o e de market basket ?? a mesma. Quando os clientes normalmente adquirem os itens ou servi??os um de cada vez (como servi??os banc??rios) chamamos de Associa????o. Quando os clientes potencialmente compram v??rias coisas de uma s?? vez chamamos de Market Basket. Assim, a An??lise da Associa????o ?? realizada ao n??vel do cliente, enquanto a An??lise de Market Basket ?? conduzida ao n??vel da transa????o. Existem tr??s etapas principais neste processo de an??lise:

  1. Avaliar a for??a da rela????o entre cada um de seus produtos e todos os outros produtos que voc?? oferece usando os algoritmos de associa????o.
  2. Identificar aqueles pares que t??m afinidade muito forte (tipicamente uma pontua????o de afinidade de 2 ou superior). Por exemplo, um cliente com um cart??o de cr??dito pode ter duas ou tr??s vezes mais probabilidade de adquirir um empr??stimo do que um cliente selecionado ao acaso.
  3. Criar uma oferta personalizada para clientes que t??m um produto (de um par de produtos fortemente associados), mas n??o o outro. 
  
Vantagens:

  ??? ?? extremamente simples e r??pido.
  ??? Funcionar?? com bases de clientes muito pequenas.
  ??? O conhecimento do cliente e seu relacionamento com produtos e servi??os n??o ?? necess??rio.
  ??? A prepara????o de dados ?? m??nima.
  ??? Associa????o e Market Basket Analysis s??o normalmente o m??todo mais rent??vel para criar ofertas personalizadas.


# Evolu????o dos Sistemas de Recomenda????o

Ao longo dos anos, os sistemas de recomenda????o evolu??ram, passaram de m??todos mais b??sicos baseados em similaridades para sistemas de recomenda????es personalizadas, de
recomenda????es baseadas em contexto, para recomenda????es em tempo real, de recomenda????es baseadas em heur??sticas b??sicas, como c??lculo de similaridade para abordagens baseadas em Machine Learning.

Nos est??gios iniciais desses sistemas de recomenda????o, apenas as classifica????es dos usu??rios sobre os produtos foram utilizadas para gerar recomenda????es. Nessa ??poca, os pesquisadores usavam apenas as informa????es de classifica????o dispon??veis. Eles simplesmente aplicaram abordagens heur??sticas como o c??lculo de similaridade usando dist??ncias euclidianas, o coeficiente de Pearson, similaridade de cosseno e etc???. Essas abordagens foram bem recebidas e, surpreendentemente, elas funcionam muito bem at?? hoje.

Esta primeira gera????o de motores de recomenda????o ?? chamada de filtragem colaborativa ou sistemas de recomenda????o de m??todos de vizinhan??a. Embora eles executem muito bem, estes sistemas v??m com seu pr??prio conjunto de limita????es, tais como problemas de Cold Start (In??cio frio), quando n??o s??o capazes de recomendar produtos a novos usu??rios sem informa????es de classifica????o. Al??m disso, esses sistemas n??o conseguem lidar com cen??rios onde os dados s??o muito escassos, de modo que as classifica????es de usu??rios dos produtos s??o muito menores.

Para superar essas limita????es, novas abordagens foram desenvolvidas. Por exemplo, a fim de lidar com problemas de conjuntos de dados muito esparsos, abordagens matem??ticas, como Fatora????o de Matriz e Singular Value Decompositions, t??m sido utilizados. S??o t??cnicas matem??ticas que ajudam a resolver problemas nos dados, aumentando a efic??cia de sistemas de recomenda????o.

No in??cio, os c??lculos de similaridade foram usados em sistemas de recomenda????o baseados em conte??do, mas com avan??os em tecnologia e infraestrutura, m??todos mais
avan??ados, como modelos de aprendizado de m??quina, substitu??ram os m??todos heur??sticos. Estes novos modelos baseados em Machine Learning melhoraram a precis??o das
recomenda????es. Embora os sistemas de recomenda????o baseados em conte??do tenham resolvido muitas das defici??ncias da filtragem colaborativa, eles t??m suas pr??prias defici??ncias inerentes, como n??o ser capaz de recomendar novos itens fora do escopo de prefer??ncia do usu??rio, o que a filtragem colaborativa poderia fazer.

Para resolver esse problema, os pesquisadores come??aram a combinar diferentes modelos de recomenda????o para chegar a modelos h??bridos, que s??o muito mais poderosos do que qualquer um dos modelos individuais. E esses modelos h??bridos atualmente englobam n??o apenas os modelos tradicionais de sistemas de recomenda????o, como t??cnicas matem??ticas e de Machine Learning, levando a sistemas totalmente personalizados a cada cliente.

Com implementa????es bem-sucedidas de mecanismos de recomenda????o personalizados, as pessoas come??aram a estender a personaliza????o a outras dimens??es chamadas contextos,
como a adi????o de localiza????o, hora, grupo e assim por diante e alteraram o conjunto de recomenda????es com cada contexto. Com avan??os em tecnologia como grandes ecossistemas de dados, ferramentas anal??ticas que executam em mem??ria e em tempo real como o Apache Spark, a capacidade de manipula????o de bancos de dados muito grandes tornou-se poss??vel. Atualmente estamos nos movendo para sistemas ainda mais personalizados com o uso de intelig??ncia artificial. No aspecto de tecnologia, as recomenda????es est??o passando de abordagens de aprendizado de m??quina para abordagens mais avan??adas de aprendizagem profunda como redes neurais.


# Sistema de Recomenda????o Baseado no Item Mais Popular

Este ?? o modelo mais simples e b??sico de sistema de recomenda????o.

A estrat??gia ?? simplesmente oferecer ao cliente o que ?? mais popular, seja um filme, um livro ou um artigo de vestu??rio. Sem fazer nada mais do que observar nos registros de vendas, ?? poss??vel construir um sistema de recomenda????o simples como esse. Isso n??o ?? necessariamente ci??ncia de dados. N??o ?? particularmente personalizado. Mas pode ser ??til se voc?? sabe muito pouco sobre o seu visitante.

Exige alguns atributos de conte??dos que podem ser usados para criar subcategorias que podem corresponder ?? navega????o atual do visitante em um site de com??rcio eletr??nico. Por exemplo, se voc?? est?? oferecendo uma grande variedade de produtos como um ??nico pacote ou combo, desde ferramentas a roupas, ou filmes, livros ou not??cias que apelam para interesses diferentes, ent??o voc?? precisar?? tentar combinar itens pelo menos na mesma categoria visualizada pelo seu visitante. Empresas como a rede de lojas Home Depot usa regularmente um espa??o em seu website chamado de "best sellers" e a GAP usa regularmente "produtos mais recentes" para indicar os produtos mais populares, indic??-los a outros consumidores e aumentar a receita. Esse tipo de sistema de recomenda????o pode ser usado como uma estrat??gia complementar a outros sistemas mais robustos.

![image](https://user-images.githubusercontent.com/79231882/206015500-27d5c773-0b03-4398-aaef-592eb09ceb04.png)


# Tipos de Sistemas de Recomenda????o

Sistemas de recomenda????o n??o s??o todos iguais. Se voc?? for implementar um sistema de recomenda????o pela primeira vez ?? muito prov??vel que voc?? comece com uma solu????o
pronta de um fornecedor ou que voc?? desenvolva seu pr??prio sistema do zero usando R ou Python por exemplo e faremos isso daqui a pouco. Al??m das quest??es t??ticas de neg??cios sobre as considera????es que devem ser feitas na implementa????o de sistemas de recomenda????o, ?? importante conhecer tecnicamente o que s??o esses sistemas. Isso significa olhar profundamente para os diferentes tipos de sistema de recomenda????o e compreender os pontos fortes e fracos de cada um.

Os tipos de sistemas de recomenda????o dependem de diferentes algoritmos.

  ??? Alguns t??m um foco maior nas semelhan??as de clientes, alguns em similaridades de conte??do e alguns uma mistura dos dois.

  ??? Diferentes algoritmos variam em sua utilidade com base no quanto voc?? sabe com anteced??ncia sobre os clientes, seu conte??do e se voc?? pode obter feedback dos clientes ap??s a compra (isso seria fundamental).

  ??? Todos devem satisfazer a exig??ncia geral de oferecer um resultado personalizado dentro de cerca de 50 milissegundos (esse ?? um desafio).

Os sistemas de recomenda????o se resumem a oferecer pontua????es aos clientes de acordo com v??rios crit??rios. Essas tags de pontua????o que voc?? coloca nos clientes e registros de conte??do raramente s??o em tempo real e s??o normalmente atualizadas durante a noite, mais ou menos frequentemente, dependendo de cada circunst??ncia e objetivo de neg??cio. Portanto, as atualiza????es de pontua????o off-line podem depender de c??lculos recomendados, mas podem ser complementadas com pontua????o e an??lise realizadas separadamente em uma escala de tempo mais longa. Ou seja, o que parece tempo real ?? na verdade quase tempo real.

![image](https://user-images.githubusercontent.com/79231882/206015872-b31afce6-6cec-4a17-a454-2e381f08d4f1.png)

Os avan??os nos sistemas de recomenda????o n??o foram t??o grandes quanto algumas outras ??reas da ci??ncia de dados. A mais complexa dessas op????es, os Filtros Colaborativos, existem a mais de dez anos. De uma perspectiva empresarial a boa not??cia ?? que voc?? pode se sentir confort??vel construindo um portf??lio de tecnologia existente e bem estabelecida. A maioria dos avan??os na ci??ncia dos dados em torno de sistemas de recomenda????o tem sido focada em melhorar gradualmente o seu desempenho nos dom??nios espec??ficos em que foram implantados. E com a grande quantidade de dados dispon??veis (Big Data), desempenho deve ser uma preocupa????o constante.
