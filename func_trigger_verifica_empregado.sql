CREATE OR REPLACE FUNCTION verifica_empregado()
RETURNS TRIGGER AS $$
DECLARE 
    tupla RECORD;
BEGIN
    SELECT COUNT(*) AS quantidade
    INTO tupla
    FROM empregados AS E, movimentacao AS M, movimentacao_empregados AS ME
    WHERE ME.id_emp = E.id_emp AND ME.id_mov = E.id_mov 
	AND NEW.id_emp = E.id_emp AND NEW.id_mov = M.id_mov
	AND M.tipo = 'Manutenção' AND E.funcao = 'Manutenção';

    IF (tupla.quantidade <> 1) THEN
    	RAISE EXCEPTION 'A função do empregado de id % não é manutenção.', NEW.id_emp;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_verifica_empregado
BEFORE INSERT OR UPDATE ON tripulantes
FOR EACH ROW
EXECUTE FUNCTION verifica_empregado();
