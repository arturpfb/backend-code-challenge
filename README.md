# Tech Challenge 

Bem vindo(a)! Esse é o Tech Challenge Python!

Aqui você terá todas as informações para o sucesso do seu desafio. Ele consiste em aplicar a linguagem Python, em conjunto com práticas em SQL.

Precisamos de pessoas com energia, integridade e inteligência, que aprendam rápido e que gostem de conhecer e aplicar novas tecnologias.

Bom desafio!

---

# O Desafio

TODO

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
* O código está em algum controle de versão?
* Os commits são pequenos e consistentes?
* As mensagens de commit são claras?

### Código Limpo

* O código possibilita expansão para novas funcionalidades?
* O código é _Don't Repeat Yourself_?
* O código é fácil de compreender?

### Controle de Qualidade (PLUS)

* O código possui testes unitários?
* O código possui teste de cobertura?
