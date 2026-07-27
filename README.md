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
- Validação de valores nulos.
- Validação de linhas duplicadas.
- Validação do intervalo da coluna `mes`.
- Validação do ano esperado.
- Validação de valores financeiros negativos.
- Resumo final das inconsistências encontradas.
- Testes realizados com dados inválidos inseridos propositalmente.

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

## Validações atuais

O script verifica:

- presença das colunas obrigatórias;
- valores nulos;
- linhas duplicadas;
- meses fora do intervalo de 1 a 12;
- anos diferentes de 2026;
- valores negativos nas colunas `valor_previsto` e `valor_arrecadado`.

Quando alguma inconsistência é encontrada, o script exibe um resumo com os problemas identificados.

## Executando o projeto

Instale e sincronize as dependências:

```bash
uv sync
```

Execute o script de leitura e validação:

```bash
uv run python scripts/read_revenues.py
```

O comando deve ser executado na raiz do projeto.

## Status do projeto

Em desenvolvimento.

As etapas de leitura, inspeção, validação estrutural e validação inicial da qualidade dos dados foram concluídas.

## Próximos passos

1. Verificar e validar os tipos esperados de cada coluna.
2. Criar o processo de limpeza e transformação dos dados.
3. Salvar os dados tratados em `data/processed`.
4. Criar o schema inicial do banco de dados PostgreSQL.
5. Carregar os dados tratados no banco.
6. Criar a API com FastAPI para consulta dos dados.