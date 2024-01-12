    # Inserir médicos
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
        inserir(cursor, "secretaria", dados_secretaria)