from pathlib import Path
import pandas as pd
import sys

file_path = Path("data/raw/revenues_2026.csv")

try:
    tabela_receitas = pd.read_csv(file_path)
    colunas_lista = tabela_receitas.columns.tolist()
except FileNotFoundError:
    print(f"Arquivo não encontrado: {file_path}")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Arquivo vazio: {file_path}")
    sys.exit(1)
except pd.errors.ParserError:
    print(f"Erro ao analisar o arquivo: {file_path}")
    sys.exit(1)
except UnicodeDecodeError:
    print(f"Erro de codificação ao ler o arquivo: {file_path}")
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
    sys.exit(1)

print("Arquivo carregado com sucesso.")

print("\nPrimeiras linhas da tabela de receitas:")
print(tabela_receitas.head())

print("\nNúmero de linhas na tabela:")
print(len(tabela_receitas))

print("\nColunas da tabela de receitas:")
print(colunas_lista)

print("\nTipos de dados das colunas:")
print(tabela_receitas.dtypes)

obrigatorias = {"ano", "mes", "codigo_receita", "nome_receita", "categoria", "fonte", "valor_previsto", "valor_arrecadado"}

faltando = obrigatorias - set(tabela_receitas.columns)

if faltando:
    raise ValueError(f"Colunas obrigatórias faltando: {faltando}")

print("Todas as colunas obrigatórias estão presentes.")

print("\nVerificando inconsistências:")

erros_detectados = []

valores_nulos = tabela_receitas.isna().sum()
total_nulos = int(valores_nulos.sum())

print(f"Valores nulos por coluna:\n{valores_nulos}")
print(f"Total de valores nulos: {total_nulos}")
if total_nulos > 0:
    erros_detectados.append("Existem valores nulos na tabela.")

linhas_duplicadas = int(tabela_receitas.duplicated().sum())
print(f"Número de linhas duplicadas: {linhas_duplicadas}")
if linhas_duplicadas > 0:
    erros_detectados.append("Existem linhas duplicadas na tabela.")

print("\nVerificando valores fora do intervalo esperado para a coluna 'mes' (1 a 12):")
meses_invalidos = tabela_receitas[(tabela_receitas['mes'] < 1) | (tabela_receitas['mes'] > 12)]
print(f"Número de linhas com 'mes' fora do intervalo: {len(meses_invalidos)}")
if len(meses_invalidos) > 0:
    erros_detectados.append("Existem valores inválidos na coluna 'mes'.")

print("\nVerificando valores negativos nas colunas 'valor_previsto' e 'valor_arrecadado':")
valores_negativos = tabela_receitas[(tabela_receitas['valor_previsto'] < 0) | (tabela_receitas['valor_arrecadado'] < 0)]
print(f"Número de linhas com valores negativos: {len(valores_negativos)}")
if len(valores_negativos) > 0:
    erros_detectados.append("Existem valores negativos nas colunas 'valor_previsto' e 'valor_arrecadado'.")

print("\nVerificando se todos os anos na coluna 'ano' são 2026:")
todos_sao_2026 = bool((tabela_receitas['ano'] == 2026).all())
print(f"Todos os anos são 2026: {todos_sao_2026}")
if not todos_sao_2026:
    erros_detectados.append("Existem anos diferentes de 2026 na coluna 'ano'.")


print("\nResumo das inconsistências encontradas:")

if not erros_detectados:
    print("\nA tabela de receitas está consistente e pronta para uso.")
else:
    print("\nA tabela de receitas apresenta inconsistências e precisa ser revisada antes do uso.")
    print("Erros detectados:")
    for erro in erros_detectados:
        print(f" - {erro}")
