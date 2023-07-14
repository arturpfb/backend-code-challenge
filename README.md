# Tech Challenge 

Bem vindo(a)! Esse é o Tech Challenge Python!

Aqui você terá todas as informações para o sucesso do seu desafio. Ele consiste em aplicar a linguagem Python, em conjunto com práticas em SQL.

Precisamos de pessoas com energia, integridade e inteligência, que aprendam rápido e que gostem de conhecer e aplicar novas tecnologias.

Bom desafio!

---

## Requisitos Técnicos

* O código do desafio está na linguagem Python, na versão 3.11.1, com o framework Flask. Como auxiliar, temos um banco em Postgres, na versão 14.1.
* Para a utilização da api cedida, será necessário você ter instalado:
  * Docker
  * Alembic
  * Poetry
* Será necessário criar um arquivo .env, do qual a api irá se basear. Cedemos um .env.example dos valores sugeridos, mas faça as alterações desejadas.

## Comandos básicos do projeto

`docker compose up --build`: Levanta a imagem da aplicação local, aceitando requisições na porta 3000, e cria uma instância do banco local, na porta 5434, com todas as migrations que constam na pasta src/migrations/versions

com o terminal na pasta migrations:

`alembic revision -m "mensagem da nova revisão"`: Cria uma nova revisão, usando como detalhamento a mensagem escrita 

# O Desafio

Primeiramente, obrigado por aceitar o desafio! Esperamos que a realização do mesmo seja proveitosa tanto para você quanto para nossa avaliação, aumentando sua capacidade de resolução de problemas.

Então, vamos ao que interessa. 

Utilizaremos como fonte para o preenchimento das nossas consultas duas apis nacionais publicas:
* Brasil api (https://brasilapi.com.br/docs)
  * Aqui, a partir da subdivisão CPTEC, obteremos informações climáticas atuais em capitais do país.
* IBGE (https://servicodados.ibge.gov.br/api/docs/agregados?versao=3)
  * Aqui, obteremos informações demográficas a respeito de diversas cidades/regiões do país.

Seu desafio é utilizar a aplicação REST em Python Flask cedida aqui para:
* Gerenciar um banco de dado Postgres, criando migrations para gerar as tabelas necessárias para a operação da api, de acordo com os dados que esta precisará ceder. O schema utilizado fica a seu critério!
* Preencher nas tabelas acima os dados demográficos e meteorológicos necessários para esta operar. Aqui, fica em aberto: Este preenchimento pode se dar por rotas nesta própria api, ou por rotinas a parte, a escolha fica a seu encargo.
* Criar os endpoints de consulta, que retornarão os dados desejados, com aceitação de parâmetros que podem ser interessantes para limitação deste retorno, como por exemplo o nome da cidade desejada.
  * Estes dados devem ser retornados em formato JSON, com todas as informações pertinentes.
  * Quais dados agregados devem ser retornados vai da sua criatividade, mas temos alguns exemplos legais:
    * Um mapa de cidades mais populosas de acordo com uma condição climática específica
    * Top X (aqui, definido por um parametro do endpoint) cidades para alguma medida, como vento ou umidade
    * Com a completude da api do IBGE, outros dados podem ser explorados, caso desejado.

Você não precisa usar TODOS os dados fornecidos pelas APIs externas, a ideia é te dar liberdade para utilizar e cruzar as informações da maneira que achar necessário.

Sinta-se à vontade para usar sua criatividade e incrementar o projeto, afinal, ele agora é seu!

## Observações adicionais

* Você é livre para utilizar quaisquer libs adicionais que desejar;
* Escreva código limpo, eficiente e fácil de dar manutenção;
* Faça os tratamentos de erro necessários, tanto nas requisições para a sua própria API quanto para as APIs externas.



## Diretrizes da aplicação

- O candidato está livre para adicionar sua própria lógica desde que mantenha a estrutura base que foi proposta.

## Critérios de Avaliação

O desafio será avaliado através de quatro critérios.

### Entrega

* O resultado final está completo para ser executado?
* O resultado final atende ao que se propõe fazer?
* O resultado final atende totalmente aos requisitos propostos?

### Boas Práticas

* O código está de acordo com o guia de estilo utilizado no resto do template?
* O código está bem estruturado?
* O código está fluente na linguagem?

### Código Limpo

* O código possibilita expansão para novas funcionalidades?
* O código é _Don't Repeat Yourself_?
* O código é fácil de compreender?

### Documentação (Desejável, porém não obrigatório)

* O código foi entregue com um arquivo de README claro de como se guiar, e dos endpoints desenvolvidos?
* Os commits são pequenos e consistentes?
* As mensagens de commit são claras?
