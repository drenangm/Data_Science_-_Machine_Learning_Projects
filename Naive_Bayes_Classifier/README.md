# Building a Naive-Bayes classifier from the scratch


# Teorema de Bayes

O Teorema de Bayes surgiu da tentativa de Bayes provar a existência de Deus

![image](https://user-images.githubusercontent.com/79231882/202478575-81d46c6e-2632-437b-a85b-c4622258fadf.png)

O teorema de Bayes fornece uma maneira de calcular a probabilidade posterior

![image](https://user-images.githubusercontent.com/79231882/202478650-5ae021a1-419c-4a29-b9ad-f4b70c98bddf.png)

![image](https://user-images.githubusercontent.com/79231882/202478773-1d434c26-011e-4713-ac79-2ebce1d0556a.png)

![image](https://user-images.githubusercontent.com/79231882/202478854-62b91d68-7847-44f1-8e71-3914e70e0143.png)

O teorema de Bayes utiliza a probabilidade condicional e sua inversa

![image](https://user-images.githubusercontent.com/79231882/202478926-8131b49d-05fe-4f41-89cd-f624af5e7cd5.png)

![image](https://user-images.githubusercontent.com/79231882/202478983-9eabc0f5-2c3d-42a7-8682-f5b0e2194078.png)

![image](https://user-images.githubusercontent.com/79231882/202479038-e65e126c-67f4-4ee2-ac02-e2f67500252a.png)

![image](https://user-images.githubusercontent.com/79231882/202479123-917c34dd-e625-4295-a219-6a6efe347087.png)

![image](https://user-images.githubusercontent.com/79231882/202479209-6468a3e4-91fe-4b1d-b3c7-76e318d4e02e.png)

Tomamos como verdadeira a ocorrência quando o valor ultrapassa um threshold, no caso acima 0.50, assim de fato aquela ocorrência pode acontecer dado o cenário apresentado.

# Problema da Frequência Zero

Vamos imaginar um cenário em um determinado valor de atributos não aparece na base treinamentos mas aparece no exemplo de teste

![image](https://user-images.githubusercontent.com/79231882/202479476-228fa4b1-5efb-41e0-9d53-9533c35a9d57.png)

Qual seria a solução para este exemplo?

→ Poderíamos adicionar 1 ao contador para cada combinação de valor classe **(estimador de Laplace)** desta forma resolveríamos o problema das probabilidades terem valor 0.

![image](https://user-images.githubusercontent.com/79231882/202479540-e6326720-eb1f-4808-98cd-3a9eea85416b.png)

