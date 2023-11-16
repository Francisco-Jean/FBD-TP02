CREATE OR REPLACE FUNCTION verifica_capitao()
RETURNS TRIGGER AS $$
BEGIN
	IF (TG_OP = 'UPDATE') THEN
		IF (NEW.funcao <> OLD.funcao) THEN
			IF ((SELECT COUNT(*) FROM tripulantes WHERE funcao = 'Capitão' AND id_emb = NEW.id_emb) = 1) THEN
				RAISE EXCEPTION 'Tripulante não atualizado. Já existe um Capitão nessa embarcação.';
			END IF;
		END IF;
	
	ELSEIF (TG_OP = 'INSERT') THEN
		IF ((SELECT COUNT(*) FROM tripulantes AS T WHERE T.funcao = 'Capitão' AND T.id_emb = NEW.id_emb) = 1) THEN
			RAISE EXCEPTION 'Tripulante não adicionado. Já existe um Capitão nessa embarcação.';
		END IF;
	END IF;
	
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_verifica_capitao
BEFORE INSERT OR UPDATE ON tripulantes
FOR EACH ROW
EXECUTE FUNCTION verifica_capitao();
