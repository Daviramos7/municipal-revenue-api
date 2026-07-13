# Municipal Revenue API

API simples para análise de receitas municipais fictícias usando Python, Pandas, PostgreSQL e FastAPI.

## Objetivo

Este projeto tem como objetivo simular um fluxo básico de tratamento, armazenamento e consulta de dados de receitas municipais.

A proposta é construir uma aplicação capaz de:

1. trabalhar com dados fictícios de receitas públicas;
2. tratar e validar os dados com Python e Pandas;
3. armazenar os dados em um banco PostgreSQL;
4. disponibilizar consultas e indicadores por meio de uma API com FastAPI.

## Tecnologias previstas

- Python
- Pandas
- PostgreSQL
- FastAPI
- Git
- GitHub

## Fluxo geral do projeto

O projeto seguirá o seguinte fluxo:

1. Criação de uma base fictícia de receitas municipais.
2. Leitura dos dados em formato CSV.
3. Tratamento e validação dos dados com Python.
4. Armazenamento dos dados tratados no PostgreSQL.
5. Criação de endpoints para consulta dos dados.
6. Documentação do projeto para apresentação no GitHub.

## Estrutura inicial

```text
municipal-revenue-api/
  app/
  data/
    raw/
    processed/
  scripts/
  docs/
  README.md
  study-log.md
  requirements.txt
  .gitignore
```

## Status do projeto
Em desenvolvimento.

## Próximos passos
1. Implementar a leitura e tratamento dos dados fictícios.
2. Criar o primeiro script de leitura dos dados.
3. Criar o processo de tratamento dos dados.
4. Criar o schema inicial do banco de dados PostgreSQL.
5. Criar a API com FastAPI para consulta dos dados.