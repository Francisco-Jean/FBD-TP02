import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Selecione o id e nome do empregado que participou de mais movimentações 
    # no Mes/Ano de uma data informada pelo usuário
    cur.execute("SELECT * FROM funcionario_do_mes('2023-10-01');")
    
    print('Funcionário do mês:')
    print(cur.fetchall())

    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()
