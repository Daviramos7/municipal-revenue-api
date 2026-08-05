from pathlib import Path
import pandas as pd

raw_file_path = Path("data/raw/revenues_2026.csv")
processed_file_path = Path("data/processed/revenues_2026_processed.csv")

tabela_original = pd.read_csv(raw_file_path)
tabela_tratada = tabela_original.copy()

tabela_tratada["ano"] = tabela_tratada["ano"].astype("int64")
tabela_tratada["mes"] = tabela_tratada["mes"].astype("int64")

tabela_tratada["codigo_receita"] = (tabela_tratada["codigo_receita"].astype("string").str.strip())

colunas_texto = [
    "nome_receita",
    "categoria",
    "fonte",
]

for coluna in colunas_texto:
    tabela_tratada[coluna] = tabela_tratada[coluna].astype("string").str.strip()

tabela_tratada["valor_previsto"] = pd.to_numeric(
    tabela_tratada["valor_previsto"],
    errors="raise",
)

tabela_tratada["valor_arrecadado"] = pd.to_numeric(
    tabela_tratada["valor_arrecadado"],
    errors="raise",
)

tabela_tratada = tabela_tratada.drop_duplicates()

processed_file_path.parent.mkdir(parents=True, exist_ok=True)

tabela_tratada.to_csv(
    processed_file_path,
    index=False,
)

print("Tipos após a transformação:")
print(tabela_tratada.dtypes)

print("\nQuantidade de registros:")
print(len(tabela_tratada))

print("\nArquivo processado salvo em:", processed_file_path)

tabela_processada = pd.read_csv(processed_file_path)

print("\nValidação do arquivo salvo:")
print("Quantidade de registros lidos:", len(tabela_processada))
print("Colunas:", tabela_processada.columns.tolist())
print("Valores nulos:", int(tabela_processada.isnull().sum().sum()))