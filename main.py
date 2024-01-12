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
    comando = "CREATE TABLE IF NOT EXISTS consulta (id integer primary key, data datetime default current_timestamp, medico_id integer, paciente_id integer, secretaria_id integer, valor real, pago boolean, FOREIGN KEY (medico_id) REFERENCES medico(id), FOREIGN KEY (paciente_id) REFERENCES paciente(id), FOREIGN KEY (secretaria_id) REFERENCES secretaria(id))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS paciente (id integer primary key, nome varchar(45), end varchar(45), telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)
    comando = "CREATE TABLE IF NOT EXISTS secretaria (id integer primary key, nome varchar(45), end varchar(45), telefone varchar(45), cpf varchar(45))"
    cursor.execute(comando)


def mostrar_tabela(cursor, nome_tabela):
    print(f"Conteúdo da Tabela {nome_tabela}:")
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    resultados = cursor.fetchall()

    if resultados:
        # Se houver resultados, imprima as linhas
        for linha in resultados:
            print(linha)
        print('\n')
    else:
        print("A tabela está vazia.")


def inserir(cursor, nome_tabela, dados):
    placeholders = ', '.join(['?' for _ in range(len(dados))])
    comando = f"INSERT INTO {nome_tabela} VALUES ({placeholders})"
    
    cursor.execute(comando, dados)
    cursor.connection.commit()

if __name__ == '__main__':
    verificacao_arquivo_bd()

    banco = conectar_bd('medico.bd')
    cursor = banco.cursor()
    criar_tabela(cursor)
    
    '''    # Inserir médicos
    for i in range(1, 6):
        dados_medico = (i, f"Médico_{i}", f"Endereço_{i}", f"12345678{i}", f"CRM{i}")
        inserir(cursor, "medico", dados_medico)

    # Inserir pacientes
    for i in range(1, 6):
        dados_paciente = (i, f"Paciente_{i}", f"Endereço_{i}", f"98765432{i}", f"CPF{i}23456789")
        inserir(cursor, "paciente", dados_paciente)

    # Inserir consultas
    for i in range(1, 6):
        dados_consulta = (i, None, i, i, i, 100.0 * i, True if i % 2 == 0 else False)
        inserir(cursor, "consulta", dados_consulta)

    # Inserir secretárias
    for i in range(1, 6):
        dados_secretaria = (i, f"Secretária_{i}", f"Endereço_{i}", f"87654321{i}", f"CPF{i}98765432")
        inserir(cursor, "secretaria", dados_secretaria)'''


    mostrar_tabela(cursor, "paciente")
    mostrar_tabela(cursor, "medico")
    mostrar_tabela(cursor, "consulta")
    mostrar_tabela(cursor, "secretaria")
    
    cursor.close()
    banco.close()

