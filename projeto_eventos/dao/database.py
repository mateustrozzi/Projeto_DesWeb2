import os
import sqlite3

caminhoBanco = "instance/eventos.db"

def conectar():
    os.makedirs("instance", exist_ok=True)
    conexao = sqlite3.connect(caminhoBanco)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS evento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_evento TEXT,
            local TEXT,
            vagas INTEGER,
            data_evento TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS participante (
            email TEXT PRIMARY KEY,
            nome TEXT,
            aluno INTEGER,
            semestre_ano TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS faz_inscricao (
            id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
            data_inscricao TEXT,
            fk_participante_email TEXT,
            fk_evento_id INTEGER,
            FOREIGN KEY (fk_participante_email) REFERENCES participante(email),
            FOREIGN KEY (fk_evento_id) REFERENCES evento(id)
        )
        """
    )

    conexao.commit()
    conexao.close()