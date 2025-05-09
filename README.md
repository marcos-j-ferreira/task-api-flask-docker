# 🐳 task-api-flask-docker

[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/python-flask-yellow)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)]()

Uma API simples de tarefas (TO-DO), criada com o propósito de consolidar o aprendizado sobre Docker, containers e deploy. A API foi feita com Flask e armazena os dados em um arquivo `JSON`.

---

## Objetivo

O foco principal deste projeto foi **praticar Docker**, desde a criação de imagens até a execução em containers. A API é propositalmente simples, permitindo que a atenção fosse direcionada à configuração, build e testes com Docker.

---

## Tecnologias utilizadas

- Python 3.11+
- Flask
- Docker
- Postman (para testes)
- JSON (como banco de dados temporário)

---

## Estrutura do Projeto

```

task-api-flask-docker/
├── app.py                  
|    ├── __init__.py         # Inicializador da API
|    ├── routes.py           # Código principal da API
|    ├── db.json             # "Banco de dados" local em JSON
|    ├── Dockerfile          # Configuração da imagem Docker
|    ├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação
├── .gitignore          # versionamento
└── start.sh            # Iniciar o ambiente virtual venv to python

````

---

## Rotas da API

| Método | Rota                   | Descrição                           |
|--------|------------------------|-------------------------------------|
| GET    | `/tarefa`              | Retorna uma resposta simples        |
| GET    | `/tarefa/listar`       | Lista todas as tarefas              |
| GET    | `/tarefa/listar/id`    | Lista uma tarefa específica por ID  |
| POST   | `/tarefa/adicionar`    | Adiciona uma nova tarefa            |
| GET    | `/tarefa/deletar`      | Deleta uma tarefa                   |
| GET    | `/tarefa/estado/`      | Marca uma tarefa como concluída     |

---

## Como rodar com Docker

### 1. Build da imagem
```bash
docker build -t task-api-flask .
````

### 2. Rodar o container

```bash
docker run -d -p 5000:5000 task-api-flask
```

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## Testes com Postman

Os testes foram realizados com o **Postman**, criando uma coleção com todas as rotas disponíveis e executando múltiplas interações. As respostas foram satisfatórias e os testes auxiliaram na validação da lógica da API e no funcionamento dentro do container Docker.

---

## Sobre o Banco de Dados

Neste projeto optei por **não utilizar um banco de dados real** (como PostgreSQL ou SQLite). Em vez disso, usei um arquivo `db.json` como armazenamento local. Isso permitiu manter o projeto mais leve e focado no principal objetivo: **praticar Docker**. Em projetos futuros, irei incluir bancos reais e ORMs.

---

## Lições aprendidas

* Criar imagens Docker personalizadas com `Dockerfile`
* Executar e testar aplicações Flask em containers
* Fazer testes automatizados com Postman
* Trabalhar com persistência de dados simples em JSON

---

## Próximos passos

* Adicionar validação nas entradas de dados
* Implementar um banco de dados real (PostgreSQL ou MongoDB)
* Criar testes automatizados com `pytest`
* Criar um docker-compose para orquestração

---

## Autor

**Marcos** – Desenvolvedor em formação, focado em backend, Cloud e Machine Learning.

---

