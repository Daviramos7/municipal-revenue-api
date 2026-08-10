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
- Psycopg
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
      revenues_2026_processed.csv
  database/
    schema.sql
  scripts/
    read_revenues.py
    transform_revenues.py
    load_revenues.py
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
- Conversão de `codigo_receita` para texto.
- Validação de conversão numérica das colunas `ano`, `mes`, `valor_previsto` e `valor_arrecadado`.
- Resumo final das inconsistências encontradas.
- Encerramento do script com código de erro quando a base é inválida.
- Testes realizados com dados inválidos inseridos propositalmente.
- Script separado de limpeza e transformação criado.
- Criação de uma cópia do DataFrame original antes das transformações.
- Padronização dos tipos das colunas.
- Limpeza de espaços no início e no final das colunas textuais.
- Remoção de linhas duplicadas.
- Criação automática do diretório `data/processed`.
- Geração do arquivo `revenues_2026_processed.csv`.
- Validação da leitura do arquivo processado.
- Confirmação da preservação dos 50 registros.
- Confirmação da ausência de valores nulos no arquivo processado.
- PostgreSQL instalado e configurado no ambiente Windows.
- Banco de dados `municipal_revenue` criado.
- Schema inicial do banco criado em `database/schema.sql`.
- Tabela `revenues` criada com tipos compatíveis com os dados processados.
- Chave primária automática criada com `BIGSERIAL`.
- Restrição para limitar a coluna `mes` ao intervalo de 1 a 12.
- Restrição de unicidade criada para `ano`, `mes` e `codigo_receita`.
- Psycopg adicionado como dependência do projeto.
- Script `scripts/load_revenues.py` criado.
- Conexão Python com PostgreSQL realizada por meio do Psycopg.
- Credenciais do banco lidas por variáveis de ambiente.
- Conversão das linhas do DataFrame em registros para inserção.
- Carga dos 50 registros processados no PostgreSQL.
- Uso de transações com `commit` e `rollback`.
- Implementação de upsert com `ON CONFLICT ... DO UPDATE SET`.
- Validação de que novas execuções do loader não duplicam registros.
- Validação de atualização de registros existentes a partir do CSV processado.
- Confirmação de 50 registros persistidos no PostgreSQL.

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

## Tipos esperados

- `ano`: número inteiro;
- `mes`: número inteiro;
- `codigo_receita`: texto;
- `nome_receita`: texto;
- `categoria`: texto;
- `fonte`: texto;
- `valor_previsto`: número decimal;
- `valor_arrecadado`: número decimal.

A coluna `codigo_receita` é tratada como texto porque representa um identificador e não um valor usado em cálculos.

## Validações atuais

O script verifica:

- presença das colunas obrigatórias;
- valores nulos;
- linhas duplicadas;
- meses fora do intervalo de 1 a 12;
- anos diferentes de 2026;
- valores negativos nas colunas `valor_previsto` e `valor_arrecadado`;
- valores que não podem ser convertidos para número nas colunas `ano`, `mes`, `valor_previsto` e `valor_arrecadado`.

Quando alguma inconsistência é encontrada, o script exibe um resumo com os problemas identificados e encerra a execução com código de erro.

## Transformações atuais

O script `scripts/transform_revenues.py` realiza:

- leitura da base bruta;
- criação de uma cópia do DataFrame original;
- conversão de `ano` e `mes` para números inteiros;
- conversão de `codigo_receita` para texto;
- conversão das colunas `nome_receita`, `categoria` e `fonte` para texto;
- remoção de espaços extras no início e no final dos textos;
- conversão de `valor_previsto` e `valor_arrecadado` para valores numéricos;
- remoção de linhas duplicadas;
- criação do diretório de dados processados, caso ele não exista;
- salvamento da base tratada em formato CSV;
- leitura do arquivo salvo para validação;
- conferência da quantidade de registros, colunas e valores nulos.

## Arquivo processado

O arquivo tratado é salvo em:

```text
data/processed/revenues_2026_processed.csv
```

O arquivo processado possui:

- 50 registros;
- 8 colunas;
- nenhum valor nulo;
- tipos padronizados para as etapas seguintes do projeto.

## Banco de dados

O projeto utiliza um banco PostgreSQL chamado:

```text
municipal_revenue
```

A tabela principal é:

```text
revenues
```

Sua estrutura é definida em:

```text
database/schema.sql
```

A tabela contém:

- `id`: chave primária automática;
- `ano`: inteiro;
- `mes`: inteiro entre 1 e 12;
- `codigo_receita`: texto;
- `nome_receita`: texto;
- `categoria`: texto;
- `fonte`: texto;
- `valor_previsto`: `NUMERIC(14, 2)`;
- `valor_arrecadado`: `NUMERIC(14, 2)`.

A combinação abaixo é única:

```text
ano + mes + codigo_receita
```

Essa restrição permite utilizar upsert durante a carga dos dados.

## Carga no PostgreSQL

O script `scripts/load_revenues.py` realiza:

- leitura do arquivo processado;
- conexão com o PostgreSQL por meio do Psycopg;
- leitura das credenciais por variáveis de ambiente;
- preparação dos registros;
- inserção em lote com `executemany`;
- confirmação da transação com `commit`;
- cancelamento da transação com `rollback` em caso de erro;
- atualização de registros existentes com `ON CONFLICT ... DO UPDATE SET`;
- prevenção de duplicação por meio da restrição única da tabela.

A carga atual possui 50 registros.

O comportamento do upsert é:

```text
registro não existe
→ INSERT

registro já existe
→ UPDATE
```

## Variáveis de ambiente

Antes de executar a carga, devem estar disponíveis as seguintes variáveis:

```text
PGHOST
PGPORT
PGDATABASE
PGUSER
PGPASSWORD
```

Exemplo no PowerShell:

```powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="municipal_revenue"
$env:PGUSER="postgres"
$env:PGPASSWORD="sua_senha"
```

A senha do PostgreSQL não é armazenada diretamente no código-fonte.

## Executando o projeto

Instale e sincronize as dependências:

```bash
uv sync
```

Execute o script de leitura e validação:

```bash
uv run python scripts/read_revenues.py
```

Execute o script de limpeza e transformação:

```bash
uv run python scripts/transform_revenues.py
```

Execute o script de carga no PostgreSQL:

```bash
uv run python scripts/load_revenues.py
```

Os comandos devem ser executados na raiz do projeto.

## Status do projeto

Em desenvolvimento.

As etapas de leitura, inspeção, validação estrutural, validação da qualidade e validação inicial dos tipos de dados foram concluídas.

A etapa de limpeza, transformação e geração da base processada também foi concluída.

A criação do schema PostgreSQL e a carga automatizada dos dados processados também foram concluídas.

O fluxo atual do projeto é:

```text
CSV bruto
→ validação
→ transformação
→ CSV processado
→ PostgreSQL
```

## Próximos passos

1. Criar um script separado para limpeza e transformação dos dados.
2. Padronizar os tipos finais das colunas.
3. Salvar os dados tratados em `data/processed`.
4. Criar o schema inicial do banco de dados PostgreSQL.
5. Carregar os dados tratados no banco.
6. Criar a API com FastAPI para consulta dos dados.

Os itens 1, 2 e 3 foram concluídos em 05/08/2026.

Os itens 4 e 5 foram concluídos em 10/08/2026.

A próxima etapa ativa é criar a API com FastAPI para consulta dos dados.