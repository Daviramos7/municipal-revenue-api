from pathlib import Path
import sys

import pandas as pd


file_path = Path("data/raw/revenues_2026.csv")

try:
    tabela_receitas = pd.read_csv(file_path)
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
except Exception as erro:
    print(f"Ocorreu um erro ao ler o arquivo: {erro}")
    sys.exit(1)


print("Arquivo carregado com sucesso.")

print("\nPrimeiras linhas da tabela de receitas:")
print(tabela_receitas.head())

print("\nNúmero de linhas na tabela:")
print(len(tabela_receitas))

print("\nColunas da tabela de receitas:")
print(tabela_receitas.columns.tolist())

print("\nTipos de dados das colunas:")
print(tabela_receitas.dtypes)


colunas_obrigatorias = {
    "ano",
    "mes",
    "codigo_receita",
    "nome_receita",
    "categoria",
    "fonte",
    "valor_previsto",
    "valor_arrecadado",
}

colunas_faltando = colunas_obrigatorias - set(tabela_receitas.columns)

if colunas_faltando:
    print(f"Colunas obrigatórias faltando: {colunas_faltando}")
    sys.exit(1)

print("Todas as colunas obrigatórias estão presentes.")


print("\nVerificando inconsistências:")

erros_detectados = []


print("\nTipos de dados das colunas antes da conversão:")
print(tabela_receitas.dtypes)

tabela_receitas["codigo_receita"] = tabela_receitas[
    "codigo_receita"
].astype(str)

print("\nTipos de dados das colunas após a conversão:")
print(tabela_receitas.dtypes)


valor_previsto_numeric = pd.to_numeric(
    tabela_receitas["valor_previsto"],
    errors="coerce",
)

valor_arrecadado_numeric = pd.to_numeric(
    tabela_receitas["valor_arrecadado"],
    errors="coerce",
)

ano_numeric = pd.to_numeric(
    tabela_receitas["ano"],
    errors="coerce",
)

mes_numeric = pd.to_numeric(
    tabela_receitas["mes"],
    errors="coerce",
)


erros_valor_previsto = int(
    valor_previsto_numeric.isna().sum()
    - tabela_receitas["valor_previsto"].isna().sum()
)

erros_valor_arrecadado = int(
    valor_arrecadado_numeric.isna().sum()
    - tabela_receitas["valor_arrecadado"].isna().sum()
)

erros_ano = int(
    ano_numeric.isna().sum()
    - tabela_receitas["ano"].isna().sum()
)

erros_mes = int(
    mes_numeric.isna().sum()
    - tabela_receitas["mes"].isna().sum()
)


if erros_valor_previsto > 0:
    erros_detectados.append(
        f"{erros_valor_previsto} valor(es) inválido(s) na coluna "
        "'valor_previsto' não puderam ser convertidos para número."
    )

if erros_valor_arrecadado > 0:
    erros_detectados.append(
        f"{erros_valor_arrecadado} valor(es) inválido(s) na coluna "
        "'valor_arrecadado' não puderam ser convertidos para número."
    )

if erros_ano > 0:
    erros_detectados.append(
        f"{erros_ano} valor(es) inválido(s) na coluna "
        "'ano' não puderam ser convertidos para número."
    )

if erros_mes > 0:
    erros_detectados.append(
        f"{erros_mes} valor(es) inválido(s) na coluna "
        "'mes' não puderam ser convertidos para número."
    )


valores_nulos = tabela_receitas.isna().sum()
total_nulos = int(valores_nulos.sum())

print(f"\nValores nulos por coluna:\n{valores_nulos}")
print(f"Total de valores nulos: {total_nulos}")

if total_nulos > 0:
    erros_detectados.append(
        f"Existem {total_nulos} valor(es) nulo(s) na tabela."
    )


linhas_duplicadas = int(tabela_receitas.duplicated().sum())

print(f"\nNúmero de linhas duplicadas: {linhas_duplicadas}")

if linhas_duplicadas > 0:
    erros_detectados.append(
        f"Existem {linhas_duplicadas} linha(s) duplicada(s) na tabela."
    )


print(
    "\nVerificando valores fora do intervalo esperado "
    "para a coluna 'mes' (1 a 12):"
)

meses_invalidos = tabela_receitas[
    (mes_numeric < 1) | (mes_numeric > 12)
]

quantidade_meses_invalidos = len(meses_invalidos)

print(
    "Número de linhas com 'mes' fora do intervalo: "
    f"{quantidade_meses_invalidos}"
)

if quantidade_meses_invalidos > 0:
    erros_detectados.append(
        f"Existem {quantidade_meses_invalidos} valor(es) fora do "
        "intervalo de 1 a 12 na coluna 'mes'."
    )


print(
    "\nVerificando valores negativos nas colunas "
    "'valor_previsto' e 'valor_arrecadado':"
)

valores_negativos = tabela_receitas[
    (valor_previsto_numeric < 0)
    | (valor_arrecadado_numeric < 0)
]

quantidade_valores_negativos = len(valores_negativos)

print(
    "Número de linhas com valores negativos: "
    f"{quantidade_valores_negativos}"
)

if quantidade_valores_negativos > 0:
    erros_detectados.append(
        f"Existem {quantidade_valores_negativos} linha(s) com valores "
        "negativos em 'valor_previsto' ou 'valor_arrecadado'."
    )


print("\nVerificando se todos os anos na coluna 'ano' são 2026:")

todos_sao_2026 = bool((ano_numeric == 2026).all())

print(f"Todos os anos são 2026: {todos_sao_2026}")

if not todos_sao_2026:
    erros_detectados.append(
        "Existem anos diferentes de 2026 na coluna 'ano'."
    )


print("\nResumo das inconsistências encontradas:")

if not erros_detectados:
    print("\nA tabela de receitas está consistente e pronta para uso.")
else:
    print(
        "\nA tabela de receitas apresenta inconsistências "
        "e precisa ser revisada antes do uso."
    )
    print("Erros detectados:")

    for erro in erros_detectados:
        print(f" - {erro}")

    sys.exit(1)