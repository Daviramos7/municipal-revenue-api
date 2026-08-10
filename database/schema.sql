CREATE TABLE IF NOT EXISTS revenues (
    id BIGSERIAL PRIMARY KEY,
    ano INTEGER NOT NULL,
    mes INTEGER NOT NULL CHECK (mes BETWEEN 1 AND 12),
    codigo_receita TEXT NOT NULL,
    nome_receita TEXT NOT NULL,
    categoria TEXT NOT NULL,
    fonte TEXT NOT NULL,
    valor_previsto NUMERIC(14, 2) NOT NULL,
    valor_arrecadado NUMERIC(14, 2) NOT NULL,

    CONSTRAINT revenues_unique_record
        UNIQUE (ano, mes, codigo_receita)
);