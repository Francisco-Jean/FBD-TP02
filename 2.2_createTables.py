import psycopg2

try:
    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=541790 user=541790 password=541790@fbd host=200.129.44.249")

    # Criação de um cursor
    cur = conn.cursor()

    # Criação das tabelas
    cur.execute("CREATE TABLE IF NOT EXISTS Embarcacoes (id_emb INT PRIMARY KEY, nome VARCHAR(50), tipo VARCHAR(50));")

    cur.execute("CREATE TABLE IF NOT EXISTS Tripulantes (id_trip INT PRIMARY KEY, nome VARCHAR(255), data_nasc DATE, funcao VARCHAR(50), id_emb INT, FOREIGN KEY (id_emb) REFERENCES Embarcacoes (id_emb));")

    cur.execute("CREATE TABLE IF NOT EXISTS Empregados (id_emp INT PRIMARY KEY, nome VARCHAR(255), data_nasc DATE, funcao VARCHAR(50));")

    cur.execute("CREATE TABLE IF NOT EXISTS Movimentacao (id_mov INT PRIMARY KEY, data DATE, tipo VARCHAR(50), id_emb INT, FOREIGN KEY (id_emb) REFERENCES Embarcacoes (id_emb));")

    cur.execute("CREATE TABLE IF NOT EXISTS Movimentacao_Empregados (id_mov INT, id_emp INT, PRIMARY KEY (id_mov, id_emp), FOREIGN KEY (id_mov) REFERENCES Movimentacao (id_mov), FOREIGN KEY (id_emp) REFERENCES Empregados (id_emp));")

    conn.commit()
    
    cur.close()
    
except psycopg2.DatabaseError as e:
    print('O seguinte erro ocorreu: %s' % e)
finally:
    if conn is not None:
        conn.close()

