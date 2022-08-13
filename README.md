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

* main.py
   
    > Arquivo para o processamento dos dados

* dash:
   
    * main.py
   
        > Para rodar o dashboar simples em python+Dash
---

## Soluções:

- Data Studio:
    
    > Dashboard feito pelo Google data studio
    
    - link de acesso: https://datastudio.google.com/s/uYbUxgcBVuQ

- Python Dash:
    
    > Uma outra opção não citada, que pode ser pensando, usando a propria lib do python, para a criação do dashboard, tendo como vantagem maior facilidade pra processamento de dados enquanto mostra, este pode ser visto como caso de estudo
    - como executar: 
        
        Para executar deve-se instalar as dependencis listadas no requirements.txt
        ``` 
            python -m pip install -r requirments.txt 
        ```

        Após as dependencias instaladas,
        para executar o Dash pasta executar o main.py da pasta
        
        ```
            python dash/main.py 
        ```
---
## considerações 

A base para plotagem foi feita usando apenas as casas e o somatório de dividas e "recursos" de cada uma, sendo classificadas em ABC de acordo com o critério definido pelo problema, como o maior interesse foram os recursos de cada casa, esses foram usados no dashboard, entretanto pode ser facilmente trocado para dividas caso necessário. 



Também foi adicionado uma nova opção de dashboard, usando dash, apenas por mais aprendizados.

