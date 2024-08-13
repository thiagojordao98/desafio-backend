CREATE TABLE Pessoas (
    idPessoa SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    dataNascimento DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    observacoes TEXT
);
