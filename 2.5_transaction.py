import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    
    
    cur.execute('''
                
                INSERT INTO Movimentacao (id_mov, data, tipo, id_emb) VALUES (6, '2023-10-05', 'Manutenção', 1);
                
                INSERT INTO Movimentacao_Empregados (id_mov, id_emp) VALUES (6, 1);
                
                SELECT COUNT(*) FROM Movimentacao AS M, Embarcacoes AS E WHERE M.id_emb = E.id_emb AND E.tipo = 'Cargueiro';
                ''')
    
    conn.commit()
    
    print('Quantidade de movimentações que envolvem embarcações do tipo "Cargueiro":')
    for row in cur:
        print(row)
    
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()