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
- uv

## Fluxo geral do projeto

O projeto seguirá o seguinte fluxo:

1. Criação de uma base fictícia de receitas municipais.
2. Leitura dos dados em formato CSV.
3. Tratamento e validação dos dados com Python.
4. Armazenamento dos dados tratados no PostgreSQL.
5. Criação de endpoints para consulta dos dados.
6. Documentação do projeto para apresentação no GitHub.

## Estrutura atual

```text
municipal-revenue-api/
  app/
  data/
    raw/
      revenues_2026.csv
    processed/
  scripts/
    read_revenues.py
  docs/
  README.md
  study-log.md
  pyproject.toml
  uv.lock
  .gitignore
```

## Progresso atual

- Estrutura inicial do projeto criada.
- Base fictícia de receitas municipais adicionada em CSV.
- Projeto Python inicializado com uv.
- Pandas adicionado como dependência.
- Script de leitura do CSV criado.
- Exibição das primeiras linhas da base.
- Contagem da quantidade de registros.
- Listagem das colunas disponíveis.
- Exibição dos tipos de dados.
- Validação das colunas obrigatórias.
- Tratamento dos principais erros de leitura do arquivo.

## Colunas esperadas

O arquivo CSV deve conter as seguintes colunas:

- `ano`
- `mes`
- `codigo_receita`
- `nome_receita`
- `categoria`
- `fonte`
- `valor_previsto`
- `valor_arrecadado`

## Executando o projeto

Instale e sincronize as dependências:

```bash
uv sync
```

Execute o script de leitura e validação:

```bash
uv run python scripts/read_revenues.py
```

## Status do projeto

Em desenvolvimento.

A etapa inicial de leitura, inspeção e validação estrutural do arquivo CSV foi concluída.

## Próximos passos

1. Validar valores ausentes e registros duplicados.
2. Verificar os tipos e intervalos dos dados.
3. Criar o processo de limpeza e transformação.
4. Salvar os dados tratados em `data/processed`.
5. Criar o schema inicial do banco de dados PostgreSQL.
6. Carregar os dados tratados no banco.
7. Criar a API com FastAPI para consulta dos dados.