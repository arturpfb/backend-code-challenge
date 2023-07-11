## Adicionando migrations

Para a adição de uma nova migration, abra o terminal e vá até a pasta de migrations:

```sh
cd src/migrations
```

Em seguida, rode o seguinte comando:

```sh
alembic revision -m "{mensagem da migration}"
```

Com este, um novo file será criado seguindo o template, e preenchendo as ordens das revisions.

Você deverá então preencher os processos de upgrade e downgrade da revision, seguindo os outros modelos (mesmo formato do nosso dbup)

Lembre-se de que as migrations serão rodadas na mesma ordem em que são inseridas, portanto siga uma ordem cronológica que não prejudique a arquitetura e subsequente uso das suas tabelas.
