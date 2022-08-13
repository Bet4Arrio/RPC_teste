# Arquivos do Teste da RPC

## Desafio:
>   Você é um renomado analista no banco de Bravos e recebeu da alta diretoria a tarefa de criar a curva ABC dos atuais correntistas do banco. Infelizmente, não existe uma integração entre as duas bases de dados disponíveis (correntistas_banco_bravos.csv e correntistas_obito.csv), dessa forma, todas as contas estão atualmente ativas não levando em consideração os óbitos. Sabendo disso, crie a curva ABC seguindo as diretrizes do banco informadas abaixo: <br> - A: >= 50%;<br> - B: >= 20% e < 50%; <br> - C: <20%; <br> O propósito da análise é demonstrar para os acionistas em quais famílias/alianças há a necessidade de intensificar o investimento para o próximo ano com base em seu patrimônio previsto para este ano.
---

## Arquivos e pastas:

* original_db:
    * correntistas_banco_bravos_1.csv
        > Base de dados fornecida com os correntistas
    * correntistas_obito_1.csv
        > Base de dados fornecida com os obitos 

* toplot
    * abc_house_all.csv
        > Classificação de grupos ABC, para dividas e receita de cada aliança.
    * abc_person_all.csv
        > Classificação de grupos ABC, para dividas e receitas para cada pessoa.

---

## Soluções:

- Data Studio:
    - link de acesso: https://datastudio.google.com/s/uYbUxgcBVuQ
        > Dashboard feito pelo Google data studio


---
## considerações 

Foi feito duas possíveis bases para plotagem, porém foi usada a que melhor se enquadra no problema a ser analisado. 


A primeira base foi feita usando apenas as casas e o somatório de dividas e "recursos" de cada uma, sendo classificadas em ABC de acordo com o critério definido pelo problema, como o maior interesse foram os recursos de cada casa, esses foram usados no dashboard, entretanto pode ser facilmente trocado para dividas caso necessário. 

  

Outra análise foi feita para cada pessoa unitariamente, este não foi usado para o dashboard, no entanto é possível fazer os mesmos gráficos para esta base sem muitas mudanças.
