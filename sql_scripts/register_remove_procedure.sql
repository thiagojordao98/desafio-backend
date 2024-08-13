CREATE OR REPLACE FUNCTION remover_pessoa(
    p_idPessoa INTEGER
)
RETURNS VARCHAR AS $$
BEGIN
    DELETE FROM Pessoas
    WHERE idPessoa = p_idPessoa;
    RETURN 'OK';
END;
$$ LANGUAGE plpgsql;
