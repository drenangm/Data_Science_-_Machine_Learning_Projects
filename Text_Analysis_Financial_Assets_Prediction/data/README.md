# Analise textual: Previsao de Ativos Financeiros


Criacao de um modelo híbrido para prever o preço de ativos financeiros usando a análise numérica dos preços históricos das ações e análise textual (especificamente análise de sentimentos) de textos de notícias


## Definição de Problema

O objetivo é criar um modelo híbrido para prever o preço de ativos financeiros usando a análise numérica dos preços históricos das ações e análise textual (especificamente análise de sentimentos) de textos de notícias. Usaremos dados da SENSEX (S&P BSE SENSEX).

Usaremos somente as manchetes das notícias. Caso usássemos cada notícia completa o processamento poderia levar dias para ser concluído.


## Fonte de dados

Foram utiizados dados disponibilizados publicamente.

Para o dataset de texto de notícias usaremos um conjunto de dados disponibilizado pelo repositório Harvard Dataverse. O dataset Times of India News Headlines é bastante recente, está em inglês e contém uma compilação de notícias sobre o cenário econômico na Índia. O dataset pode ser encontrado no link abaixo:

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DPQMQH

Para os dados e cotação de ações, extraímos o dataset do portal http://finance.yahoo.com/. Os dados seguem o padrão de cotações de ações com data, valor de abertura da cotação, valor de fechamento, valor mais alto, valor mais baixo e valor ajustado. Cada linha representa um dia de cotação.
