CREATE OR REPLACE FUNCTION inserir_pessoa(
    p_nome VARCHAR(255),
    p_dataNascimento DATE,
    p_salario DECIMAL(10, 2),
    p_observacoes TEXT,
    p_nomeMae VARCHAR(255),
    p_nomePai VARCHAR(255),
    p_cpf VARCHAR(11)
)
RETURNS INTEGER AS $$
DECLARE
	new_id INTEGER;
BEGIN
    INSERT INTO Pessoas (nome, dataNascimento, salario, observacoes, nomeMae, nomePai, cpf)
    VALUES (p_nome, p_dataNascimento, p_salario, p_observacoes, p_nomeMae, p_nomePai, p_cpf)
    RETURNING idPessoa INTO new_id;
	RETURN new_id;
END;
$$ LANGUAGE plpgsql;


    

