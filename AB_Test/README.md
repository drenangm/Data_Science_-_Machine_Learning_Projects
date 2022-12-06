# A/B Test


Contribuicao do Teste A/B na avaliacao da performance de uma pagina de vendas de produtos online

O Teste A/B, ou teste de divisão, é um método eficaz em Marketing Digital, como técnica de otimização, para tentar gradualmente aumentar as conversões do funil de vendas (contatos ou vendas). Ou ainda melhorar outras fases iniciais como, por exemplo, taxa de cliques ou taxa de rejeição. 

Um Teste A/B consiste em testar duas diferentes estratégias em um grupo específico.

Para ilustrar, digamos que você tenha uma página de venda de livros online com um botão para o usuário se cadastrar e receber seus e-mails–esse elemento é chamado de controle (o elemento existente).

Você quer saber se algo pode ser melhorado na página, para atrair mais inscritos. De todas as estratégias de Marketing, a comunicação via e-mail ainda é a mais eficiente.

Então, você cria outra página com um botão de inscrição diferente –você pode mudar o lugar do botão, a cor, o texto call-to-action, o formato, etc. Este novo elemento é chamado variável.

Agora, você exibe as duas versões da página para divisão 50/50 de toda sua audiência. Ou seja, todos os seus usuários visualizarão o botão de cadastro, mas alguns visualizarão a página onde o botão é azul e outros visualizarão a página onde o botão é verde, por exemplo. 

Desta forma, você reunirá os dados analíticos das duas versões, a controle e a variável, e poderá usar como fator decisivo. Qual deles pode trazer mais inscritos?

O que obteve mais resultados deve ser o escolhido.

Isso é apenas a ponta do iceberg! Podemos usar Teste A/B em diversas plataformas de marketing, como social media, marketing visual e muito mais. 


# Funcionamento de Testes A/B

Um exemplo clássico de Teste A/B é mudar a cor de um botão. Digamos que um botão seja azul, mas um Gerente de Marketing vem com uma ótima ideia: o que aconteceria se o tornássemos verde?

O botão azul é a versão A, a versão atual, o controle. O botão verde é a versão B, a nova versão, o teste. Queremos saber: o botão verde é tão incrível quanto pensamos? É uma experiência melhor para nossos usuários? Isso leva a melhores resultados para o nosso negócio? Para descobrir, executamos um Teste A/B. Atribuímos aleatoriamente alguns usuários para ver a versão A e alguns para ver a versão B. Em seguida, medimos algumas métricas de resultados principais para os usuários em cada grupo. Finalmente, usamos a análise estatística para comparar essas métricas entre os dois grupos e determinar se os resultados são significativos.

A significância estatística é uma maneira formal de medir se um resultado é interessante. Sabemos que existe uma variabilidade natural em nossos usuários. Nem todo mundo se comporta exatamente da mesma maneira. Portanto, queremos verificar se a diferença entre A e B pode ser apenas devido ao acaso. Finja que, em vez disso, executamos um Teste A/A (isso mesmo, A/A). Dividimos aleatoriamente os usuários em dois grupos, mas todos recebem o botão azul. Há uma gama de diferenças (perto de zero) que poderíamos esperar ver. Quando os resultados do Teste A/B são estatisticamente significativos, isso significa que seria muito incomum ver em um teste A/A. Nesse caso, concluiríamos que o botão verde fez a diferença.

Para fazer compras em um portal online, os usuários precisam criar uma conta. Exigir que nossos usuários façam login é ótimo para Testes A/B e para análises em geral. Isso significa que podemos unir todas as ações de um usuário por meio de seu ID de conta, mesmo se ele trocar de navegador ou dispositivo. Isso torna mais fácil medir comportamentos de longo prazo, muito além de uma única sessão. E, como podemos medi-los, podemos fazer um teste A/B para eles.

Um dos resultados comuns que medimos em qualquer negócio é o processo de compra. Um resultado de curto prazo seria: quanto esse usuário gastou na sessão ao ver o botão azul ou verde? Um resultado de longo prazo seria: quanto o usuário gastou durante o Teste A/B? Sempre que um usuário vê o controle ou a experiência de teste, dizemos que eles foram expostos. Um usuário pode ser exposto repetidamente no decorrer de um teste. Acumulamos métricas de resultado desde a primeira exposição até o final do teste. Ao medir os resultados cumulativos, podemos entender melhor o impacto de longo prazo e não nos distrair com os efeitos da novidade.


# Como analisar testes A/B?

## Elevacao (Lift)

Normalmente, a análise de Teste A/B mede a diferença entre a versão B e a versão A. Para uma métrica de resultado x, a diferença entre o teste e o controle é xB - xA. Essa diferença, especialmente para resultados cumulativos, pode aumentar com o tempo. Considere o exemplo de gasto por usuário exposto. Conforme o Teste A/B continua, os dois grupos continuam comprando e acumulando mais gastos. A versão B é um sucesso se os gastos do grupo de teste aumentarem mais rápido do que os de controle.

Em vez da diferença, medimos a elevação (Lift) de B sobre A. A elevação dimensiona a diferença pelo valor da linha de base. Para uma métrica de resultado x, a elevação do teste sobre o controle é:




![image](https://user-images.githubusercontent.com/79231882/183440949-e8ad6570-15a7-417d-bc9c-38b20e18579b.png)



Descobrimos que o aumento das métricas cumulativas tende a ser estável ao longo do tempo. Isso é o que chamamos de Lift.


## Analise de Potencia

Antes de iniciar um Teste A/B, é bom fazer duas perguntas: 


1- Que porcentagem de usuários deve fazer o teste versus o controle?

2- Quanto tempo o teste precisa ser executado?

A maneira estatística formal de responder a essas perguntas é uma análise de potência. Primeiro, precisamos saber qual é a menor diferença (ou aumento) que seria significativo para o negócio. Isso é chamado de tamanho do efeito. Em segundo lugar, precisamos saber o quanto a métrica de resultado normalmente flutua. A análise de potência calcula o tamanho da amostra, o número de usuários necessários para detectar esse tamanho de efeito com significância estatística.

Existem dois componentes para usar o tamanho da amostra. A divisão é a fração de usuários em teste versus controle e isso afeta o tamanho da amostra necessário. O tempo para o teste é o tempo total que levará para expor tantos usuários. Como os usuários podem voltar e serem expostos novamente, o número cumulativo exposto aumentará mais lentamente com o passar do tempo. Matematicamente, quanto mais desequilibrada a divisão (quanto mais distante de 50-50 em qualquer direção), mais longo será o teste. Da mesma forma, quanto menor o tamanho do efeito, mais longo será o teste.

Muitas vezes, a análise de potência não conta toda a história. Por exemplo, se em um portal online temos um forte ciclo semanal - as pessoas compram de maneira diferente nos fins de semana dos dias de semana.

É recomendável a execução de Testes A/B por pelo menos uma semana e, de preferência, em múltiplos de sete dias. Obviamente, se os resultados parecerem drasticamente negativos após o primeiro ou dois dias, é bom desligar o teste mais cedo.

O equilíbrio da divisão afeta a duração da execução do teste, mas também consideramos o nível de risco. Se tivermos uma grande quantidade de produtos à venda, podemos começar com 90% de controle, 10% de teste. Por outro lado, se quisermos ter certeza de que um recurso importante no site continua fornecendo sustentação, podemos manter um controle de 5% e teste de 95%. Mas, se tivermos um teste de baixo risco, como uma pequena mudança na interface do site, uma divisão em 50% do controle, o teste de 50% significará um tempo de teste mais curto.


Em geral, realizamos esses 5 passos para analisar um Teste A/B:


1. Configuramos o experimento.

2. Executamos o teste de hipóteses e registramos a taxa de sucesso de cada grupo.

3. Criamos o Plot da distribuição da diferença entre as duas amostras.

4. Calculamos o poder estatístico.

5. Avaliamos como o tamanho das amostras afeta os Testes A/B.


