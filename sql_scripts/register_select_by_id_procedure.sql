CREATE OR REPLACE FUNCTION selecionar_registro(
    p_idPessoa INTEGER
) RETURNS TABLE(idPessoa INTEGER, nome VARCHAR, dataNascimento DATE, salario DECIMAL, observacoes TEXT, nomeMae VARCHAR, nomePai VARCHAR, cpf VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT 
        p.idPessoa, 
        p.nome, 
        p.dataNascimento, 
        p.salario, 
        p.observacoes, 
        p.nomeMae, 
        p.nomePai, 
        p.cpf 
    FROM Pessoas p 
    WHERE p.idPessoa = p_idPessoa;
END;
$$ LANGUAGE plpgsql;
