import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Tenta inserir novas movimentações_empregados
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (5, 5);")
    conn.commit()
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (5, 2);")
    conn.commit()
    
    # Tenta modificar o valor do atributo 'funcao' do Tripulante3 para 'Capitão'
    cur.execute("UPDATE Tripulantes SET funcao = 'Capitão' WHERE id_trip = 3;")
    conn.commit()
    
    # Tenta inserir  os novos tripulantes
    cur.execute("INSERT INTO Tripulantes VALUES (7, 'Tripulante7', '1980-09-04', 'Capitão', 4);")
    conn.commit()
    
    cur.execute("INSERT INTO Tripulantes VALUES (8, 'Tripulante8', '1985-03-03', 'Capitão', 2);")
    conn.commit()
    
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()