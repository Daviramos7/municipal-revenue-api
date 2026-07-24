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