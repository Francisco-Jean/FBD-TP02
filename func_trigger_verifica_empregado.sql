CREATE OR REPLACE FUNCTION verifica_empregado()
RETURNS TRIGGER AS $$
DECLARE 
    mov RECORD;
	emp RECORD;
BEGIN
    SELECT *
    INTO mov
    FROM movimentacao AS M
    WHERE M.id_mov = NEW.id_mov;
	
	IF (mov.tipo = 'Manutenção') THEN
	
	    SELECT *
		INTO emp
		FROM empregados AS E
		WHERE E.id_emp = NEW.id_emp;
		
		IF (emp.funcao <> 'Manutenção') THEN
			RAISE EXCEPTION 'A função do empregado de id % não é manutenção.', NEW.id_emp;
		END IF;
	END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_verifica_empregado
BEFORE INSERT OR UPDATE ON movimentacao_empregados
FOR EACH ROW
EXECUTE FUNCTION verifica_empregado();
