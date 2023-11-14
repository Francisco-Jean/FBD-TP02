import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Tenta inserir novas movimentações_empregados
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (5, 5);")
    
    cur.execute("INSERT INTO Movimentacao_Empregados VALUES (5, 2);")
    
    conn.commit()
    
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()