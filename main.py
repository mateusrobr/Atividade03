import pathlib
import os
import sqlite3

def verificacao_arquivo_bd():
    nome_arquivo = os.getcwd() + "\\medico.bd"
    if os.path.exists(nome_arquivo):
        pass
    else:
        with open(nome_arquivo, 'w') as fp:
            pass

def conectar_bd(nome_bd: str):
    conexao = sqlite3.connect(nome_bd)
    return conexao

def criar_tabela(cursor):
    comando = "CREATE TABLE IF NOT EXISTS "+"medico"+" (id integer, nome varchar(45), end varchar(45), telefone varchar(45), crm varchar(45))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS "+"consulta"+" (id integer, data datetime default current_timestamp, medico_id integer, paciente_id integer, secretaria_id integer, valor real, pago boolean)"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS "+"consulta"+" (id integer, data datetime default current_timestamp, medico_id integer, paciente_id integer, secretaria_id integer, valor real, pago boolean)"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS "+"paciente"+" (id integer, nome varchar(45), end varchar(45), paciente_id integer, telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS "+"secretaria"+" (id integer, nome varchar(45), end varchar(45), telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)

if __name__ == '__main__':
    verificacao_arquivo_bd()

    banco = conectar_bd('medico.bd')
    cursor = banco.cursor()
    criar_tabela(cursor)
    banco.close()

