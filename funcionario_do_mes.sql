CREATE OR REPLACE FUNCTION funcionario_do_mes(data_analise DATE)
RETURNS TABLE (
	id_emp INT,
	nome VARCHAR
) AS $$
BEGIN
	RETURN QUERY
	WITH Quantidades AS (
		SELECT E.id_emp, E.nome, COUNT(E.id_emp) AS quantidade_mov
		FROM Empregados AS E, Movimentacao_Empregados AS ME, Movimentacao AS M
		WHERE E.id_emp = ME.id_emp AND ME.id_mov = M.id_mov 
		    AND DATE_PART('month', M.data) = DATE_PART('month', data_analise) 
			AND DATE_PART('year', M.data) = DATE_PART('year', data_analise)
		GROUP BY E.id_emp, E.nome)
	
	SELECT Q.id_emp, Q.nome FROM Quantidades AS Q
	WHERE Q.quantidade_mov = (SELECT MAX(quantidade_mov) FROM Quantidades);
	
END; $$ LANGUAGE plpgsql;
