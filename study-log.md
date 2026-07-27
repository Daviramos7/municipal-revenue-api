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

### Próximo passo

Validar os tipos esperados de cada coluna e iniciar o processo de limpeza e transformação dos dados.