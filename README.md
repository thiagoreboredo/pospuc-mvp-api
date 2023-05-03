# pospuc-mvp-api
API (Back-End) do MVP da Pós Graduação na PUC Rio

Criação de uma API (Back-End) em Python 3, usando os frameworks Flask e Flask OpenAPI para funcionalidades de um MVC, e o SQL Alchemy como ORM.

A persistência é feita usando SQLite para diminuir a complexidade com um banco de dados externo.

---
## Como executar 

Para a execução, será necessário ter todas as libs python que estão listadas no `requirements.txt` instaladas.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://127.0.0.1:5000/#/](http://127.0.0.1:5000/#/) no navegador para verificar o status da API em execução.

Ao abrir pode escolher a documentação em Swagger, com todo o detalhamento de funcionamento dos endpoints