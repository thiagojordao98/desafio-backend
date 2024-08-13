CREATE OR REPLACE FUNCTION atualizar_pessoa(
    p_idPessoa INTEGER,
    p_nome VARCHAR(255),
    p_dataNascimento DATE,
    p_salario DECIMAL(10, 2),
    p_observacoes TEXT,
    p_nomeMae VARCHAR(255),
    p_nomePai VARCHAR(255),
    p_cpf VARCHAR(11)
) RETURNS TEXT AS $$
BEGIN
    UPDATE Pessoas
    SET nome = p_nome,
        dataNascimento = p_dataNascimento,
        salario = p_salario,
        observacoes = p_observacoes,
        nomeMae = p_nomeMae,
        nomePai = p_nomePai,
        cpf = p_cpf
    WHERE idPessoa = p_idPessoa;
    
    RETURN 'OK';
END;
$$ LANGUAGE plpgsql;
