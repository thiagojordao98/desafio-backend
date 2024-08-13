CREATE OR REPLACE FUNCTION selecionar_todos_registros()
RETURNS TABLE(idPessoa INTEGER, nome VARCHAR(255), dataNascimento DATE, salario DECIMAL(10, 2), observacoes TEXT, nomeMae VARCHAR(255), nomePai VARCHAR(255), cpf VARCHAR(11))
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM Pessoas;
END;
$$ LANGUAGE plpgsql;
