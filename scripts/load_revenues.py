from pathlib import Path
import os

import pandas as pd
import psycopg


processed_file_path = Path("data/processed/revenues_2026_processed.csv")

tabela_processada = pd.read_csv(processed_file_path)

print("Arquivo processado carregado com sucesso.")
print("Quantidade de registros:", len(tabela_processada))


conn = psycopg.connect(
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT"),
    dbname=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD")
)

print("Conexão com o PostgreSQL realizada com sucesso.")


cursor = conn.cursor()


insert_query = """
INSERT INTO revenues (
    ano,
    mes,
    codigo_receita,
    nome_receita,
    categoria,
    fonte,
    valor_previsto,
    valor_arrecadado
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (ano, mes, codigo_receita) DO UPDATE SET
    nome_receita = EXCLUDED.nome_receita,
    categoria = EXCLUDED.categoria,
    fonte = EXCLUDED.fonte,
    valor_previsto = EXCLUDED.valor_previsto,
    valor_arrecadado = EXCLUDED.valor_arrecadado
"""


registros = []

for _, linha in tabela_processada.iterrows():
    registro = (
        int(linha["ano"]),
        int(linha["mes"]),
        str(linha["codigo_receita"]),
        str(linha["nome_receita"]),
        str(linha["categoria"]),
        str(linha["fonte"]),
        float(linha["valor_previsto"]),
        float(linha["valor_arrecadado"])
    )

    registros.append(registro)


try:
    cursor.executemany(insert_query, registros)
    conn.commit()

    print("Registros carregados com sucesso:", len(registros))

except Exception as erro:
    conn.rollback()

    print("Erro ao carregar registros:", erro)


cursor.close()
conn.close()