import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Inserção das Embarcações
    cur.execute("INSERT INTO Embarcacoes VALUES (1, 'Navio1', 'Cargueiro');")
    
    cur.execute("INSERT INTO Embarcacoes VALUES (2, 'Navio2', 'Passageiro');")
    
    cur.execute("INSERT INTO Embarcacoes VALUES (3, 'Navio3', 'Petroleiro');")
    
    cur.execute("INSERT INTO Embarcacoes VALUES (4, 'Navio4', 'Cargueiro');")
    
    # Inserção dos Tripulantes
    cur.execute("INSERT INTO Tripulantes VALUES (1, 'Tripulante1', '1990-01-15', 'Oficial de Convés', 1);")
    
    cur.execute("INSERT INTO Tripulantes VALUES (2, 'Tripulante2', '1992-03-20', 'Engenheiro', 1);")
    
    cur.execute("INSERT INTO Tripulantes VALUES (3, 'Tripulante3', '1988-11-05', 'Comissário de Bordo', 2);")
    
    cur.execute("INSERT INTO Tripulantes VALUES (4, 'Tripulante4', '1995-06-30', 'Oficial de Convés', 3);")
    
    cur.execute("INSERT INTO Tripulantes VALUES (5, 'Tripulante5', '1991-07-10', 'Capitão', 4);")
    
    cur.execute("INSERT INTO Tripulantes VALUES (6, 'Tripulante6', '1994-09-25', 'Engenheiro', 4);")
    
    # Inserção dos Empregados
    cur.execute("INSERT INTO Empregados VALUES (1, 'Employee1', '1985-05-12', 'Manutenção');")
    
    cur.execute("INSERT INTO Empregados VALUES (2, 'Employee2', '1993-02-28', 'Segurança');")
    
    cur.execute("INSERT INTO Empregados VALUES (3, 'Employee3', '1987-09-18', 'Logística');")
    
    cur.execute("INSERT INTO Empregados VALUES (4, 'Employee4', '1990-12-05', 'Limpeza');")
    
    cur.execute("INSERT INTO Empregados VALUES (5, 'Employee5', '2001-08-30', 'Manutenção');")
    
    # Inserção das Movimentações
    cur.execute("INSERT INTO Movimentacao VALUES (1, '2023-09-01', 'Carga', 1);")
    
    cur.execute("INSERT INTO Movimentacao VALUES (2, '2023-09-02', 'Embarque de Passageiros', 2);")
    
    cur.execute("INSERT INTO Movimentacao VALUES (3, '2023-10-03', 'Abastecimento', 3);")
    
    cur.execute("INSERT INTO Movimentacao VALUES (4, '2023-10-05', 'Descarga', 1);")
    
    cur.execute("INSERT INTO Movimentacao VALUES (5, '2023-10-05', 'Manutenção', 4);")
    
    # Inserção dos Empregados nas Movimentações
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (1, 1);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (1, 3);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (2, 2);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (3, 1);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (3, 4);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (4, 1);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (4, 3);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (5, 1);")
    
    conn.commit()
    
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()