CREATE OR REPLACE FUNCTION verifica_capitao()
RETURNS TRIGGER AS $$
DECLARE 
    tupla RECORD;
BEGIN
    SELECT COUNT(*) AS quantidade
    INTO tupla
    FROM tripulantes
    WHERE funcao = 'Capitão' AND id_emb = NEW.id_emb;

    IF (tupla.quantidade > 1) THEN
        IF (TG_OP = 'INSERT') THEN
            RAISE EXCEPTION 'Tripulante não adicionado. Já existe um Capitão nessa embarcação.';
        END IF;

        IF (TG_OP = 'UPDATE') THEN
            RAISE EXCEPTION 'Tripulante não atualizado. Já existe um Capitão nessa embarcação.';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_verifica_capitao
BEFORE INSERT OR UPDATE ON tripulantes
FOR EACH ROW
EXECUTE FUNCTION verifica_capitao();
