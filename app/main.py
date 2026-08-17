import os
import psycopg
from fastapi import FastAPI
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_connection():
    return psycopg.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        row_factory=dict_row
    )

@app.get("/")
def root():
    return {"message": "Municipal Revenue API"}

@app.get("/revenues")
def list_revenues():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            ano,
            mes,
            codigo_receita,
            nome_receita,
            categoria,
            fonte,
            valor_previsto,
            valor_arrecadado
        FROM revenues
        ORDER BY id
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows