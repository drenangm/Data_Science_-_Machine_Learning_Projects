# Predicting real-time financial assets with pyspark and machine learning

Using historical data from the Ethereum quotation, we will try to predict the quotation values of this cryptocurrency, which has been receiving a lot of attention from the investor market in recent years due to its extensive ecosystem.


The data was obtained from the source below:


<b>[https://ethereuprice.org/](https://ethereumprice.org/)</b>


The data are attached but can also be extracted from this source.


This project was carried out simulating a distributed computing environment, using the Spark framework, which offers a great solution for distributed computing.
Spark was developed in Scala language but has a framework developed for Python called Pyspark.

With Pyspark we can extract data in different formats, convert them into a spark dataframe to read this data in a distributed environment.

In practice, the database is small, which would not justify the use of a distribution strategy for processing this data in a distributed environment, but like any asset that evolves over time, over the years this base it will grow a lot this way, beforehand, we would already have a development base prepared to meet this requirement.

We used Pandas only for exploratory analysis, as Psypark was not developed to serve as a data exploration tool, but rather as a data processing tool in a distributed environment.

Fell free to explore more visions, expand this database and extract another insights.
