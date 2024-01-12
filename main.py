import pathlib
import os
import sqlite3

def verificacao_arquivo_bd():
    nome_arquivo = os.getcwd() + "\\medico.bd"
    print(nome_arquivo)
    if os.path.exists(nome_arquivo):
        pass
    else:
        with open(nome_arquivo, 'w') as fp:
            pass

def conectar_bd(nome_bd: str):
    conexao = sqlite3.connect(nome_bd)
    return conexao

def criar_tabela(cursor):
    comando = "CREATE TABLE IF NOT EXISTS medico (id integer primary key, nome varchar(45), end varchar(45), telefone varchar(45), crm varchar(45))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS consulta (id integer primary key, data datetime default current_timestamp, medico_id integer, paciente_id integer, secretaria_id integer, valor real, pago boolean)"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS consulta (id integer primary key, data datetime default current_timestamp, medico_id integer, paciente_id integer, secretaria_id integer, valor real, pago boolean)"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS paciente (id integer primary key, nome varchar(45), end varchar(45), telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS secretaria (id integer primary key, nome varchar(45), end varchar(45), telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)



if __name__ == '__main__':
    verificacao_arquivo_bd()

    banco = conectar_bd('medico.bd')
    cursor = banco.cursor()
    criar_tabela(cursor)
    #PRA INSERIR USA ESSE DIGITA ESSE COMANDO AQUI EMBAIXO E DPS COLOCA ELE ALI NO EXECUTE 
    comando = "INSERT INTO paciente VALUES (?,?,?,?,?)"
    cursor.execute(comando,(1,"Christian","Augusto Montenegro","9198245421","014454544545"))
    #PRA FAZER MUDANÇAS NO BANCO TEM QUE USAR O COMIIT
    banco.commit()

    
    
    print("Tabela Paciente")
    cursor.execute("SELECT * FROM paciente")
    print(cursor.fetchall())
    print("-------------------------")
    print("Tabela Medico")
    cursor.execute("SELECT * FROM medico")
    print(cursor.fetchall())
    print("-------------------------")
    print("Tabela Consulta")
    cursor.execute("SELECT * FROM consulta")
    print(cursor.fetchall())
    print("-------------------------")
    print("Tabela Secretaria")
    cursor.execute("SELECT * FROM secretaria")
    print(cursor.fetchall())
    print("-------------------------")
    cursor.close()
    banco.close()

