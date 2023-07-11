# Tech Challenge 

Bem vindo(a)! Esse é o Tech Challenge Python!

Aqui você terá todas as informações para o sucesso do seu desafio. Ele consiste em aplicar a linguagem Python, em conjunto com práticas em SQL.

Precisamos de pessoas com energia, integridade e inteligência, que aprendam rápido e que gostem de conhecer e aplicar novas tecnologias.

Bom desafio!

---

# O Desafio

Primeiramente, obrigado por aceitar o desafio! Esperamos que a realização do mesmo seja proveitosa tanto para nossa avaliação como para você, aumentando sua capacidade de resolução de problemas ou até mesmo colocando mais um projeto em seu portfólio.

Então, vamos ao que interessa: seu desafio é criar uma aplicação em Python que consome uma API pública de meteorologia e uma API pública de dados geográficos e, a partir daí, performa análises e tarefas variadas utilizando Python e SQL. A estrutura base da aplicação já existe, queremos que você dedique seu tempo criando a conexão da aplicação com as APIs externas e realizando as tarefas esperadas. Sinta-se à vontade para usar sua criatividade e incrementar o projeto, afinal, ele agora é seu!

* Utilize as APIs OpenWeatherMap (https://openweathermap.org/) e GeoNames API (http://www.geonames.org/export/web-services.html) para realizar o desafio;
* Utilizando PostgreSQL e rodando as migrations localmente, crie tabela(s) que serão responsáveis por armazenar os dados meteorológicos e geográficos. Aqui, a modelagem do banco fica a seu critério -- respeitando, é claro, padrões de tipos de dados e etc;
* Crie um endpoint com uma rota GET, que recebe como parâmetro o nome de uma cidade. Faça requisições nas APIs externas para buscar informações geográficas e meteorológicas relacionadas à essa cidade;
* Guarde essas informações no banco;
* Retorne um json com informações pertinentes da cidade/meteorologia;
* Crie parâmetros e/ou rotas adicionais (fica a seu critério) considerando tanto condições climáticas quanto locais específicos para buscar informações como:
  * Um mapa de cidades mais populosas de acordo com um clima específico;
  * A temperatura média, umidade, velocidade do vento e etc de uma cidade dado um range de datas;
  * (BONUS) Qualquer parâmetro adicional que você queira aceitar para performar análises nas tabelas e realizar requisições diferentes nas APIs externas.

## Observações adicionais

* Você é livre para utilizar quaisquer libs adicionais que desejar;
* Escreva código limpo, eficiente e fácil de dar manutenção;
* Faça os tratamentos de erro necessários, tanto nas requisições para a sua própria API quanto para as APIs externas.

## Requisitos Técnicos

* O código do desafio está na linguagem Python, na versão 3.11.1, com o framework Flask. Como auxiliar, temos um banco em Postgres, na versão 14.1.

## Comandos básicos do projeto

`docker compose up --build` Levanta a imagem da aplicação local, aceitando requisições na porta 3000, e cria uma instância do banco local, na porta 5434, com todas as migrations que constam na pasta src/migrations/versions

com o terminal na pasta migrations:

`alembic revision -m "mensagem da nova revisão"` Cria uma nova revisão, usando como detalhamento a mensagem escrita 

## Diretrizes da aplicação

- O candidato está livre para adicionar sua própria lógica desde que mantenha a estrutura base que foi proposta.

## Critérios de Avaliação

O desafio será avaliado através de cinco critérios.

### Entrega

* O resultado final está completo para ser executado?
* O resultado final atende ao que se propõe fazer?
* O resultado final atende totalmente aos requisitos propostos?

### Boas Práticas

* O código está de acordo com o guia de estilo utilizado no resto do template?
* O código está bem estruturado?
* O código está fluente na linguagem?

### Documentação

* O código foi entregue com um arquivo de README claro de como se guiar?
* O código possui comentários pertinentes?
* Os commits são pequenos e consistentes?
* As mensagens de commit são claras?

### Código Limpo

* O código possibilita expansão para novas funcionalidades?
* O código é _Don't Repeat Yourself_?
* O código é fácil de compreender?

### Controle de Qualidade (PLUS)

* O código possui testes unitários?
* O código possui teste de cobertura?
