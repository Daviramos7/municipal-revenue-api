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