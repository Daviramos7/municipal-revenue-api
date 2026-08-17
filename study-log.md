# Study Log

Registro de estudos e evolução do projeto Municipal Revenue API.

## 16/07/2026 — Prática de SQL

### O que foi feito

Foram criadas consultas SQL para análise de uma tabela fictícia de receitas municipais.

As consultas desenvolvidas incluem:

1. total arrecadado por mês;
2. total previsto e arrecadado por categoria;
3. diferença entre arrecadado e previsto;
4. percentual de realização por categoria;
5. top 5 categorias por arrecadação;
6. meses abaixo do valor previsto;
7. total arrecadado por fonte;
8. ranking de categorias;
9. arrecadação acumulada por mês;
10. comparação entre o mês atual e o mês anterior.

### Conceitos praticados

- `SELECT`
- `SUM`
- `GROUP BY`
- `ORDER BY`
- `HAVING`
- `LIMIT`
- `RANK`
- `LAG`
- funções de janela
- `OVER`
- CTE com `WITH`

### Dificuldades encontradas

- Diferença entre agrupamento e função de janela.
- Uso de agregações dentro de `OVER`.
- Comparação do mês atual com o anterior usando `LAG`.
- Criação de uma CTE para separar o total mensal da comparação temporal.

---

## 24/07/2026 — Leitura e validação inicial do CSV

### O que foi feito

- Criei o script `scripts/read_revenues.py`.
- Li o arquivo `data/raw/revenues_2026.csv` com Pandas.
- Exibi as primeiras linhas da base.
- Verifiquei a quantidade de registros.
- Listei as colunas disponíveis.
- Exibi os tipos de dados.
- Validei a presença das colunas obrigatórias.
- Adicionei mensagens para facilitar a leitura do resultado no terminal.
- Adicionei tratamento para os principais erros de leitura.

### Colunas obrigatórias validadas

- `ano`
- `mes`
- `codigo_receita`
- `nome_receita`
- `categoria`
- `fonte`
- `valor_previsto`
- `valor_arrecadado`

### Erros tratados

- arquivo não encontrado;
- arquivo vazio;
- erro de análise do CSV;
- erro de codificação;
- outros erros inesperados.

### Conceitos praticados

- `pandas.read_csv`
- DataFrame
- `head`
- `len`
- `columns`
- `tolist`
- `dtypes`
- conjuntos em Python
- diferença entre conjuntos
- `try` e `except`
- `sys.exit`
- `pathlib.Path`

### Dificuldades encontradas

- O Pandas não estava instalado no ambiente usado pelo projeto.
- A instalação global estava bloqueada porque o Python era gerenciado pelo uv.
- Foi necessário inicializar o projeto com uv e adicionar o Pandas como dependência.
- O caminho inicial do CSV estava incorreto.
- O tratamento de erro precisava envolver diretamente a chamada de `read_csv`.
- A leitura com `open` era redundante, porque o Pandas já realizava a leitura do arquivo.

### Resultado

A leitura, inspeção e validação estrutural inicial do arquivo CSV foram concluídas.

O script passou a conseguir:

- carregar a base;
- apresentar informações básicas;
- verificar as colunas obrigatórias;
- encerrar com mensagens claras em caso de erro.

---

## 27/07/2026 — Validação da qualidade dos dados

### O que foi feito

- Adicionei a verificação de valores nulos por coluna.
- Calculei o total de valores nulos da base.
- Adicionei a contagem de linhas duplicadas.
- Validei se os meses estão entre 1 e 12.
- Validei se todos os registros pertencem ao ano de 2026.
- Validei se existem valores negativos em `valor_previsto` ou `valor_arrecadado`.
- Criei uma lista para registrar as inconsistências detectadas.
- Adicionei um resumo final informando se a base está válida ou precisa ser revisada.

### Validações implementadas

- valores nulos;
- linhas duplicadas;
- meses fora do intervalo esperado;
- anos diferentes de 2026;
- valores financeiros negativos.

### Conceitos praticados

- `isna`
- `sum`
- `duplicated`
- filtros com condições booleanas
- operadores `|` e `<`
- `all`
- conversão com `int` e `bool`
- listas em Python
- `append`
- `if`, `else` e `not`
- repetição com `for`

### Testes realizados

Foi criada temporariamente uma versão do CSV com inconsistências propositais:

- 1 valor nulo;
- 1 linha duplicada;
- 1 mês igual a 13;
- 1 valor financeiro negativo;
- 1 ano diferente de 2026.

O script detectou corretamente todos os problemas e exibiu as mensagens esperadas no resumo final.

Depois dos testes, o arquivo CSV original foi restaurado e a validação voltou a aprovar a base.

### Dificuldades encontradas

- Diferenciar a contagem de registros válidos da identificação de registros inválidos.
- Verificar se todos os valores da coluna `ano` eram iguais a 2026.
- Somar o total de nulos a partir do resultado por coluna.
- Evitar repetir todas as condições no `if` final.
- Entender que o script deve ser executado a partir da raiz do projeto por causa do caminho relativo do CSV.

### Resultado

A etapa de validação inicial da qualidade dos dados foi concluída.

O script agora consegue:

- identificar inconsistências;
- informar a quantidade de problemas encontrados;
- listar os tipos de erros detectados;
- aprovar a base quando nenhuma inconsistência existe.

---

## 29/07/2026 — Validação e padronização inicial dos tipos

### O que foi feito

- Inspecionei os tipos carregados pelo Pandas.
- Identifiquei que `codigo_receita` estava sendo lido como número inteiro.
- Converti `codigo_receita` para texto por se tratar de um identificador.
- Criei versões numéricas temporárias das colunas:
  - `ano`;
  - `mes`;
  - `valor_previsto`;
  - `valor_arrecadado`.
- Usei conversão segura para identificar valores que não podem ser interpretados como números.
- Integrei os erros de conversão à lista `erros_detectados`.
- Ajustei a ordem das validações para evitar comparações numéricas com textos inválidos.
- Passei a usar as séries convertidas nas validações de intervalo, ano e valores negativos.
- Mantive o resumo das inconsistências como última etapa do script.
- Adicionei encerramento com código de erro quando a base possui inconsistências.

### Tipos esperados

- `ano`: inteiro;
- `mes`: inteiro;
- `codigo_receita`: texto;
- `nome_receita`: texto;
- `categoria`: texto;
- `fonte`: texto;
- `valor_previsto`: decimal;
- `valor_arrecadado`: decimal.

### Conceitos praticados

- `astype`
- `pd.to_numeric`
- `errors="coerce"`
- conversão de identificadores para texto
- criação de séries numéricas temporárias
- comparação entre nulos antes e depois da conversão
- prevenção de erros de tipo
- ordem de execução das validações
- reutilização de variáveis convertidas
- códigos de saída com `sys.exit`

### Dificuldades encontradas

- Entender que `codigo_receita` deve ser texto mesmo sendo formado apenas por números.
- Diferenciar conversão temporária de alteração da coluna original.
- Calcular quantos novos valores nulos surgiram por falha de conversão.
- Evitar que comparações como `< 0` ou `> 12` fossem executadas sobre textos.
- Posicionar o resumo final somente depois de todas as validações.
- Evitar sobrescrever as séries numéricas com DataFrames ou valores booleanos.
- Utilizar as versões convertidas nas validações posteriores.

### Resultado

A validação inicial dos tipos de dados foi concluída.

O script agora consegue:

- tratar `codigo_receita` como identificador textual;
- detectar valores não numéricos nas colunas esperadas;
- continuar a validação sem quebrar ao encontrar textos inválidos;
- incluir falhas de conversão no resumo de inconsistências;
- encerrar com código de erro quando a base não está válida.

### Próximo passo

Criar um script separado para limpeza e transformação dos dados, padronizar os tipos finais e salvar a base tratada em `data/processed`.

---

## 05/08/2026 — Limpeza, transformação e geração da base processada

### Retomada do projeto

O projeto foi retomado em um notebook com Linux, sem uma cópia local anterior do repositório.

Antes de continuar o desenvolvimento, foi necessário:

- confirmar a instalação do Git;
- instalar e configurar o `uv`;
- autenticar a conta do GitHub com o GitHub CLI;
- clonar o repositório;
- recriar o ambiente virtual;
- instalar as dependências registradas no projeto;
- executar novamente o script de validação.

O script `scripts/read_revenues.py` foi executado com sucesso e confirmou que a base original possuía:

- 50 registros;
- todas as colunas obrigatórias;
- nenhum valor nulo;
- nenhuma linha duplicada;
- nenhum mês fora do intervalo esperado;
- nenhum valor financeiro negativo;
- somente registros do ano de 2026.

### O que foi feito

- Criei o script `scripts/transform_revenues.py`.
- Defini o caminho da base bruta.
- Defini o caminho do arquivo processado.
- Li o arquivo `data/raw/revenues_2026.csv`.
- Criei uma cópia do DataFrame original antes de iniciar as transformações.
- Converti as colunas `ano` e `mes` para `int64`.
- Converti `codigo_receita` para o tipo `string`.
- Converti as colunas `nome_receita`, `categoria` e `fonte` para `string`.
- Removi espaços extras no início e no final dos valores textuais.
- Converti `valor_previsto` e `valor_arrecadado` para valores numéricos.
- Configurei a conversão numérica para gerar erro caso algum valor inválido fosse encontrado.
- Removi linhas completamente duplicadas.
- Criei automaticamente o diretório `data/processed`, caso ele não existisse.
- Salvei a tabela tratada em `data/processed/revenues_2026_processed.csv`.
- Li novamente o arquivo processado para validar o resultado.
- Verifiquei a quantidade de registros do arquivo salvo.
- Verifiquei as colunas presentes no arquivo salvo.
- Verifiquei a quantidade total de valores nulos.

### Tipos finais utilizados durante a transformação

- `ano`: `int64`;
- `mes`: `int64`;
- `codigo_receita`: `string`;
- `nome_receita`: `string`;
- `categoria`: `string`;
- `fonte`: `string`;
- `valor_previsto`: `float64`;
- `valor_arrecadado`: `float64`.

### Conceitos praticados

- `DataFrame.copy`
- `astype`
- tipo `string` do Pandas
- `str.strip`
- listas em Python
- repetição com `for`
- acesso dinâmico a colunas
- `pd.to_numeric`
- `errors="raise"`
- `drop_duplicates`
- `Path.parent`
- `mkdir`
- `parents=True`
- `exist_ok=True`
- `DataFrame.to_csv`
- `index=False`
- leitura de um arquivo processado para validação
- separação entre dados brutos e dados processados

### Diferença entre os scripts

O script `scripts/read_revenues.py` é responsável pela inspeção e validação dos dados.

Ele identifica problemas, mas não gera uma nova versão tratada da base.

O script `scripts/transform_revenues.py` é responsável pela limpeza, transformação e geração do arquivo processado.

A separação entre os scripts representa um fluxo semelhante ao de um pipeline ETL:

```text
dados brutos
→ leitura e validação
→ limpeza e transformação
→ dados processados
```

### Dificuldades encontradas

- O repositório ainda não existia no notebook Linux.
- A autenticação do GitHub por senha não funcionou, porque operações Git por HTTPS exigem outro método de autenticação.
- Foi necessário usar o GitHub CLI para autenticar e clonar o repositório.
- O caminho inicial usado no novo script apontava para `revenues.csv`, mas o nome correto era `revenues_2026.csv`.
- Foi necessário entender a diferença entre validar uma base e transformar uma base.
- Foi necessário entender por que uma cópia do DataFrame deve ser criada antes das transformações.
- O método de salvamento foi inicialmente escrito como `tocsv`, mas o nome correto é `to_csv`.
- Um comando do terminal foi colocado junto ao código Python e precisou ser executado separadamente.
- Foi necessário compreender o uso de `index=False` para impedir a criação de uma coluna adicional no CSV.
- Foi necessário compreender que `codigo_receita` deve ser texto por representar um identificador.

### Testes realizados

O script foi executado com sucesso e apresentou os seguintes tipos:

```text
ano                   int64
mes                   int64
codigo_receita       string
nome_receita         string
categoria            string
fonte                 string
valor_previsto      float64
valor_arrecadado    float64
```

O arquivo processado foi criado em:

```text
data/processed/revenues_2026_processed.csv
```

A validação do arquivo salvo apresentou:

- 50 registros;
- 8 colunas;
- nenhum valor nulo;
- estrutura compatível com a base original.

### Resultado

A etapa de limpeza e transformação dos dados foi concluída.

O projeto agora possui uma separação clara entre:

- base bruta;
- validação;
- transformação;
- base processada.

O script agora consegue:

- preservar a base original;
- padronizar os tipos das colunas;
- limpar os campos textuais;
- remover linhas duplicadas;
- gerar o diretório de saída automaticamente;
- salvar uma nova versão processada;
- validar se o arquivo gerado pode ser lido corretamente;
- confirmar que os registros e as colunas foram preservados.

### Próximo passo

Criar o schema inicial do banco de dados PostgreSQL e preparar o carregamento da base processada.

---

## 10/08/2026 — PostgreSQL, persistência e carga automatizada

### Retomada no Windows

O projeto foi retomado em um computador Windows.

Antes de iniciar a nova etapa, foi necessário:

- executar `git pull` para sincronizar o repositório com as alterações feitas anteriormente no Linux;
- executar `uv sync`;
- executar novamente `scripts/read_revenues.py`;
- executar novamente `scripts/transform_revenues.py`;
- confirmar que a base continuava válida;
- confirmar que o arquivo processado continuava com 50 registros e nenhum valor nulo.

### Configuração do PostgreSQL

O PostgreSQL ainda não estava instalado no ambiente Windows.

Foi necessário:

- instalar o PostgreSQL 18;
- confirmar a execução do serviço `postgresql-x64-18`;
- localizar o executável `psql.exe`;
- adicionar temporariamente o diretório do PostgreSQL ao `PATH` da sessão;
- testar a conexão com o servidor pelo `psql`;
- utilizar o usuário administrativo `postgres`.

### Banco criado

Foi criado o banco:

```text
municipal_revenue
```

Depois da criação, a conexão foi alterada para o novo banco utilizando o `psql`.

### Schema inicial

Foi criada a tabela `revenues` com as seguintes colunas:

- `id`;
- `ano`;
- `mes`;
- `codigo_receita`;
- `nome_receita`;
- `categoria`;
- `fonte`;
- `valor_previsto`;
- `valor_arrecadado`.

Os principais tipos utilizados foram:

- `BIGSERIAL` para o identificador;
- `INTEGER` para ano e mês;
- `TEXT` para identificadores e campos descritivos;
- `NUMERIC(14, 2)` para os valores financeiros.

### Restrições implementadas

Foram utilizadas as seguintes restrições:

- `PRIMARY KEY` em `id`;
- `NOT NULL` nos campos obrigatórios;
- `CHECK (mes BETWEEN 1 AND 12)`;
- `UNIQUE (ano, mes, codigo_receita)`.

A restrição de unicidade passou a identificar cada registro pela combinação:

```text
ano + mes + codigo_receita
```

O schema foi versionado em:

```text
database/schema.sql
```

### Primeira carga manual

Antes da automação em Python, a base processada foi carregada manualmente com `\copy`.

Foram carregados:

```text
50 registros
```

Depois da carga foram executadas consultas para:

- conferir a quantidade de registros;
- visualizar os primeiros registros;
- calcular o total arrecadado por mês.

### Dependência PostgreSQL no Python

Foi adicionado o Psycopg ao projeto.

O objetivo foi permitir que o Python se conectasse diretamente ao PostgreSQL.

### Script de carga

Foi criado:

```text
scripts/load_revenues.py
```

O script realiza:

- leitura do CSV processado com Pandas;
- abertura de conexão com PostgreSQL;
- criação de um cursor;
- preparação dos registros;
- execução da carga;
- confirmação da transação;
- tratamento de erros;
- fechamento dos recursos utilizados.

### Variáveis de ambiente

As configurações de conexão não foram colocadas diretamente no código.

Foram utilizadas as variáveis:

- `PGHOST`;
- `PGPORT`;
- `PGDATABASE`;
- `PGUSER`;
- `PGPASSWORD`.

Isso permitiu manter a senha do PostgreSQL fora do código versionado.

### Conceitos praticados

- PostgreSQL
- `psql`
- criação de banco de dados
- `CREATE DATABASE`
- `CREATE TABLE`
- `PRIMARY KEY`
- `BIGSERIAL`
- `NOT NULL`
- `CHECK`
- `UNIQUE`
- `NUMERIC`
- `\copy`
- Psycopg
- conexão Python → PostgreSQL
- variáveis de ambiente
- `os.getenv`
- conexão com `psycopg.connect`
- cursor
- `INSERT`
- placeholders `%s`
- `iterrows`
- tuplas
- `executemany`
- transações
- `commit`
- `rollback`
- `ON CONFLICT`
- `DO UPDATE SET`
- `EXCLUDED`
- upsert

### Preparação dos registros

As linhas do DataFrame foram percorridas e convertidas em tuplas contendo:

- ano;
- mês;
- código da receita;
- nome da receita;
- categoria;
- fonte;
- valor previsto;
- valor arrecadado.

Esses registros foram armazenados em uma lista e enviados ao PostgreSQL utilizando:

```text
executemany
```

### Transações

A carga foi protegida com `try` e `except`.

Quando a operação é concluída corretamente:

```text
commit
```

confirma as alterações.

Caso algum erro seja encontrado:

```text
rollback
```

desfaz a transação.

### Upsert

A carga foi alterada para utilizar:

```sql
ON CONFLICT (ano, mes, codigo_receita)
DO UPDATE SET
```

Com isso, o comportamento passou a ser:

```text
registro não existe
→ INSERT

registro já existe
→ UPDATE
```

Os seguintes campos são atualizados quando o registro já existe:

- `nome_receita`;
- `categoria`;
- `fonte`;
- `valor_previsto`;
- `valor_arrecadado`.

### Testes realizados

#### Carga pelo Python

A tabela foi limpa temporariamente para testar a carga automatizada.

O script inseriu:

```text
50 registros
```

A consulta:

```sql
SELECT COUNT(*) FROM revenues;
```

confirmou a presença de 50 registros.

#### Teste contra duplicação

O script foi executado novamente sem limpar a tabela.

A quantidade permaneceu:

```text
50 registros
```

confirmando que a restrição única impediu duplicações.

#### Teste de atualização

Um valor de `valor_arrecadado` foi alterado manualmente no PostgreSQL para:

```text
1.00
```

Depois da execução de `scripts/load_revenues.py`, o valor retornou para:

```text
792450.35
```

Esse teste confirmou que o `DO UPDATE SET` estava atualizando registros existentes com os dados presentes no arquivo processado.

### Resultado

A etapa de persistência em PostgreSQL e carga automatizada foi concluída.

O fluxo atual do projeto passou a ser:

```text
CSV bruto
→ leitura e validação
→ limpeza e transformação
→ CSV processado
→ carga automatizada
→ PostgreSQL
```

O projeto agora consegue:

- validar dados brutos;
- transformar e padronizar os dados;
- gerar uma base processada;
- conectar Python ao PostgreSQL;
- carregar os dados automaticamente;
- impedir duplicação de registros;
- atualizar registros existentes;
- utilizar transações para preservar a consistência do banco;
- manter credenciais fora do código-fonte.

### Próximo passo

Criar a API com FastAPI para consultar os dados armazenados no PostgreSQL.

---

## 17/08/2026 — FastAPI e primeira consulta ao PostgreSQL pela API

### O que foi feito

Foi iniciada a camada de API do projeto utilizando FastAPI.

Nesta etapa:

- FastAPI foi adicionada como dependência do projeto;
- Uvicorn foi adicionado como servidor para execução da aplicação;
- foi criado o arquivo `app/main.py`;
- foi criada a instância principal da aplicação FastAPI;
- foi criado o endpoint `GET /`;
- a aplicação foi executada com Uvicorn;
- a documentação automática do FastAPI foi acessada pelo Swagger;
- foi criado o endpoint `GET /revenues`;
- a API foi conectada ao PostgreSQL utilizando Psycopg;
- foi criada uma função específica para abrir conexões com o banco;
- foi executada uma consulta `SELECT` pela API;
- os resultados foram recuperados com `fetchall`;
- foi utilizado `dict_row` para retornar registros estruturados;
- os 50 registros do PostgreSQL foram retornados em JSON;
- o endpoint foi validado com resposta HTTP `200`.

### Estrutura inicial da aplicação

Foi criado:

```text
app/
  main.py
```

O arquivo passou a concentrar inicialmente:

- criação da aplicação FastAPI;
- função de conexão com PostgreSQL;
- endpoint raiz;
- endpoint de listagem de receitas.

### Endpoint raiz

Foi criado:

```http
GET /
```

O endpoint retorna:

```json
{
  "message": "Municipal Revenue API"
}
```

Essa rota foi utilizada inicialmente para confirmar que o servidor estava funcionando.

### Uvicorn

A aplicação passou a ser executada com:

```bash
uv run uvicorn app.main:app --reload
```

O parâmetro `--reload` permite reiniciar automaticamente o servidor durante o desenvolvimento quando alterações são detectadas nos arquivos.

### Swagger

A documentação automática criada pelo FastAPI foi acessada em:

```text
http://127.0.0.1:8000/docs
```

A interface permitiu visualizar e testar os endpoints diretamente pelo navegador.

### Conexão com PostgreSQL

Foi criada uma função para centralizar a abertura da conexão com o banco.

A função utiliza:

- `PGHOST`;
- `PGPORT`;
- `PGDATABASE`;
- `PGUSER`;
- `PGPASSWORD`.

Isso evita repetir a configuração da conexão em cada endpoint.

### Endpoint de receitas

Foi criado:

```http
GET /revenues
```

O endpoint:

1. abre uma conexão com o PostgreSQL;
2. cria um cursor;
3. executa uma consulta SQL;
4. recupera todas as linhas;
5. fecha o cursor;
6. fecha a conexão;
7. retorna os resultados pela API.

A consulta seleciona:

- `id`;
- `ano`;
- `mes`;
- `codigo_receita`;
- `nome_receita`;
- `categoria`;
- `fonte`;
- `valor_previsto`;
- `valor_arrecadado`.

Os registros são ordenados pelo `id`.

### `dict_row`

Foi utilizado:

```python
from psycopg.rows import dict_row
```

e configurado `row_factory=dict_row`.

Com isso, cada registro passou a ser retornado com os nomes das colunas, em vez de apenas pela posição dos valores.

### Configuração com `.env`

Durante os testes da API, foi identificado que as variáveis de ambiente configuradas manualmente no PowerShell não permaneciam disponíveis ao abrir uma nova sessão.

Para resolver isso, foi adicionada a dependência:

```text
python-dotenv
```

Foi criado um arquivo local:

```text
.env
```

contendo as configurações necessárias para conexão com o PostgreSQL.

O arquivo foi adicionado ao `.gitignore` para evitar o versionamento de informações sensíveis.

Também foi criado:

```text
.env.example
```

com:

```env
PGHOST=localhost
PGPORT=5432
PGDATABASE=municipal_revenue
PGUSER=postgres
PGPASSWORD=
```

O `.env.example` pode ser versionado porque não contém a senha real.

### Segurança das credenciais

A senha do PostgreSQL continua fora do código-fonte.

O fluxo passou a ser:

```text
.env
→ python-dotenv
→ variáveis de ambiente
→ os.getenv
→ psycopg.connect
```

### Erros encontrados

Ao adicionar `row_factory=dict_row`, inicialmente faltou uma vírgula depois do parâmetro `password`, causando um `SyntaxError`.

Depois da correção da sintaxe, a API retornou `500 Internal Server Error` porque `PGPASSWORD` não estava disponível na sessão atual do terminal.

A criação do `.env` com `python-dotenv` eliminou a necessidade de configurar manualmente as variáveis em cada nova sessão.

### Conceitos praticados

- FastAPI
- aplicação web
- endpoint
- rota HTTP
- `GET`
- Uvicorn
- servidor ASGI
- Swagger
- OpenAPI
- função de conexão com banco
- Psycopg dentro de uma API
- cursor
- `SELECT`
- `fetchall`
- `dict_row`
- `row_factory`
- JSON
- código HTTP `200`
- código HTTP `500`
- variáveis de ambiente
- `.env`
- `.env.example`
- `.gitignore`
- `python-dotenv`
- `load_dotenv`
- separação entre configuração e código

### Testes realizados

A aplicação foi iniciada com:

```bash
uv run uvicorn app.main:app --reload
```

O endpoint `GET /revenues` foi executado e retornou `HTTP 200`.

Os dados foram apresentados como uma lista de objetos JSON contendo os registros existentes no PostgreSQL.

Os 50 registros persistidos anteriormente ficaram disponíveis por meio da API.

Também foi confirmado por `git status` que o arquivo `.env` não estava sendo rastreado pelo Git.

### Resultado

A primeira etapa da API foi concluída.

O projeto agora possui o fluxo:

```text
CSV bruto
→ validação
→ transformação
→ CSV processado
→ carga automatizada
→ PostgreSQL
→ FastAPI
→ resposta JSON
```

A aplicação consegue:

- iniciar um servidor HTTP;
- expor endpoints;
- conectar ao PostgreSQL;
- executar consultas SQL;
- recuperar registros;
- converter os resultados para objetos estruturados;
- retornar os dados em JSON;
- carregar configurações locais por `.env`;
- manter credenciais sensíveis fora do repositório.

### Próximo passo

Adicionar parâmetros e filtros ao endpoint `GET /revenues`, permitindo consultas como:

```text
GET /revenues?ano=2026
GET /revenues?mes=1
GET /revenues?categoria=IPTU
```

Depois disso, iniciar endpoints de indicadores e modelos de resposta com Pydantic.

