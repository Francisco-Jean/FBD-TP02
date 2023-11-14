import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Retorne todas as embarcações e o número de tripulantes de cada embarcação
    cur.execute("SELECT E.id_emb, E.nome, E.tipo, COUNT(T.id_trip) FROM Embarcacoes AS E, Tripulantes AS T WHERE E.id_emb = T.id_emb GROUP BY E.id_emb, E.nome, E.tipo;")
    
    print('Embarcações e o número de tripulantes de cada embarcação:')
    for row in cur:
        print(row)
    print('\n')
    
    # Retorne os empregados envolvidos na movimentação de ID 1
    cur.execute("SELECT E.* FROM Empregados AS E, Movimentacao_Empregados AS ME WHERE ME.id_mov = 1 AND ME.id_emp = E.id_emp;")
    
    print('Empregados envolvidos na movimentação de ID 1:')
    for row in cur:
        print(row)
    print('\n')
    
    # Retorne a quantidade de movimentações que envolvem embarcações do tipo "Cargueiro"
    cur.execute("SELECT COUNT(*) FROM Movimentacao AS M, Embarcacoes AS E WHERE M.id_emb = E.id_emb AND E.tipo = 'Cargueiro';")
    
    print('Quantidade de movimentações que envolvem embarcações do tipo "Cargueiro":')
    for row in cur:
        print(row)
        
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()