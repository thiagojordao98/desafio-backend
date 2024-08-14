# 🛠️ Desafio Desenvolvedor Backend

Objetivo: Criar uma aplicação CRUD(create, read, update, delete) com banco de dados e API.

## 📝 Sumário

- [⚙️ Pré-requisitos](#pré-requisitos)
- [🚀 Configuração do Projeto](#configuração-do-projeto)
- [▶️ Rodando o Projeto](#rodando-o-projeto)
- [🏆 Desafio A - Banco de Dados](#desafio-a---banco-de-dados)
- [🗄️ Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [🌐 Rotas da API](#rotas-da-api)
- [🧪 Testando com Postman](#testando-com-postman)

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL 12+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)
- [Postman](https://www.postman.com/downloads/)

## 🚀 Configuração do Projeto

### 1. Clone o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/thiagojordao98/desafio-backend.git
cd desafio-backend
```

### 2. Crie e Ative um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate   # No Windows use `venv\Scripts\activate`
```

### 3. Instale as Dependências

Instale as dependências do projeto usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione a URL de conexão com o banco de dados:

```env
DATABASE_URL=postgresql://seu_usuario:senha@localhost/nome_do_banco
```

Substitua `seu_usuario`, `senha`, e `nome_do_banco` pelas suas credenciais e nome do banco de dados PostgreSQL.

### 5. Configure o Banco de Dados

Execute os scripts SQL contidos na pasta `sql_scripts` para criar a tabela e as funções necessárias:

```bash
psql -U seu_usuario -d nome_do_banco -a -f sql_scripts/create_table_pessoas.sql
...
```

## ▶️ Rodando o Projeto

### 1. Inicie o Servidor Flask

Inicie o servidor de desenvolvimento Flask:

```bash
python run.py
```

O servidor estará disponível em `http://localhost:5000`.

## 🏆 Desafio A - Banco de Dados

Este desafio envolve a criação de uma estrutura de banco de dados em PostgreSQL, incluindo a definição de tabelas, procedimentos armazenados (procedures), e índices. A seguir estão os detalhes das tarefas a serem realizadas e os scripts SQL associados.

### 1. **Criação da Tabela `Pessoas`**

Crie a tabela `Pessoas` com os seguintes campos:

- `idPessoa` (PK)
- `nome`
- `dataNascimento`
- `salario`
- `observacoes`

**Script SQL:**

```sql
CREATE TABLE Pessoas (
    idPessoa SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    dataNascimento DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    observacoes TEXT
);
```

### 2. **Alteração da Tabela `Pessoas`**

Altere a tabela `Pessoas` para adicionar os campos:

- `nomeMae`
- `nomePai`
- `cpf`

**Script SQL:**

```sql
ALTER TABLE Pessoas
ADD COLUMN nomeMae VARCHAR(255),
ADD COLUMN nomePai VARCHAR(255),
ADD COLUMN cpf VARCHAR(11);
```

### 3. **Adição de Índices de Pesquisa**

Adicione índices para melhorar a performance das buscas nos campos `nome` e `dataNascimento`.

**Script SQL:**

```sql
CREATE INDEX idx_nome ON Pessoas (nome);
CREATE INDEX idx_dataNascimento ON Pessoas (dataNascimento);
```

### 4. **Adição de Índice/Chave Única**

Garanta que o campo `cpf` seja único na tabela `Pessoas`.

**Script SQL:**

```sql
ALTER TABLE Pessoas
ADD CONSTRAINT unique_cpf UNIQUE (cpf);
```

### 5. **Criação de Procedures**

Abaixo estão as procedures a serem criadas no banco de dados.

#### a) **Procedure para Inserção de Registros**

Esta procedure insere um novo registro na tabela `Pessoas` e retorna o `idPessoa`.

**Script SQL:**

```sql
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
```

#### b) **Procedure para Atualização de Registros**

Esta procedure atualiza um registro existente na tabela `Pessoas` e retorna `OK`.

**Script SQL:**

```sql
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
```

#### c) **Procedure para Remoção de Registros**

Esta procedure remove um registro da tabela `Pessoas` e retorna `OK`.

**Script SQL:**

```sql
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
```

#### d) **Procedure para Seleção de Todos os Registros**

Esta procedure retorna todos os registros da tabela `Pessoas`.

**Script SQL:**

```sql
CREATE OR REPLACE FUNCTION selecionar_todos_registros()
RETURNS TABLE(idPessoa INTEGER, nome VARCHAR(255), dataNascimento DATE, salario DECIMAL(10, 2), observacoes TEXT, nomeMae VARCHAR(255), nomePai VARCHAR(255), cpf VARCHAR(11))
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM Pessoas;
END;
$$ LANGUAGE plpgsql;
```

#### e) **Procedure para Obter um Registro Específico**

Esta procedure retorna um registro específico da tabela `Pessoas` com base no `idPessoa`.

**Script SQL:**

```sql
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
```

### 🛠️ Scripts para uso das procedures

Aqui estão os exemplos de uso das procedures que foram criadas:

- **Inserir Pessoa:**
  ```sql
  SELECT inserir_pessoa(
      'Mariana Silva Souza', 
      '1980-01-02', 
      4000.00, 
      'CLT', 
      'Maria Clara Silva', 
      'Pedro de Souza', 
      '12345638931'
  );
  ```

- **Atualizar Pessoa:**
  ```sql
  SELECT atualizar_pessoa(
      1, 
      'Nome Atualizado', 
      '1980-01-01', 
      6000.00, 
      'Observações atualizadas', 
      'Nome da Mãe Atualizado', 
      'Nome do Pai Atualizado', 
      '12345678901'
  );
  ```

- **Remover Pessoa:**
  ```sql
  SELECT remover_pessoa(1);
  ```

- **Selecionar Todos os Registros:**
  ```sql
  SELECT selecionar_todas_pessoas();
  ```

- **Selecionar um Registro Específico:**
  ```sql
  SELECT obter_pessoa(1);
  ```

### ✅ Checklist de Testes

- [x] Inserir dados na tabela `Pessoas` através da procedure `inserir_pessoa`.
- [x] Atualizar dados na tabela `Pessoas` através da procedure `atualizar_pessoa`.
- [x] Remover dados na tabela `Pessoas` através da procedure `remover_pessoa`.
- [x] Selecionar todos os registros na tabela `Pessoas` através da procedure `selecionar_todas_pessoas`.
- [x] Selecionar um registro específico na tabela `Pessoas` através da procedure `obter_pessoa`.


## 🗄️ Estrutura do Banco de Dados

A tabela `Pessoas` possui a seguinte estrutura:

| Campo          | Tipo      | Descrição                        |
| -------------- | --------- | -------------------------------- |
| `idPessoa`     | `INTEGER` | Chave primária                   |
| `nome`         | `VARCHAR` | Nome da pessoa                   |
| `dataNascimento` | `DATE`   | Data de nascimento               |
| `salario`      | `NUMERIC` | Salário da pessoa                |
| `observacoes`  | `TEXT`    | Observações adicionais           |
| `nomeMae`      | `VARCHAR` | Nome da mãe                      |
| `nomePai`      | `VARCHAR` | Nome do pai                      |
| `cpf`          | `VARCHAR` | CPF único (Chave única)          |

## 🌐 Rotas da API

Abaixo estão as rotas disponíveis na API e suas descrições:

### 1. **Criar uma Pessoa**

- **Método:** `POST`
- **URL:** `/pessoas`
- **Descrição:** Cria um novo registro de pessoa.
- **Body:**

  ```json
  {
      "nome": "João Silva",
      "dataNascimento": "1980-01-01",
      "salario": 5000.00,
      "observacoes": "CLT",
      "nomeMae": "Maria Silva",
      "nomePai": "José Silva",
      "cpf": "12345678900"
  }
  ```

- **Resposta:**

  ```json
  {
      "idPessoa": 1
  }
  ```

### 2. **Atualizar uma Pessoa**

- **Método:** `PUT`
- **URL:** `/pessoas/{idPessoa}`
- **Descrição:** Atualiza um registro de pessoa existente.
- **Body:**

  ```json
  {
      "nome": "João Silva Atualizado",
      "dataNascimento": "1980-01-01",
      "salario": 5500.00,
      "observacoes": "PJ",
      "nomeMae": "Maria Silva",
      "nomePai": "José Silva",
      "cpf": "12345678900"
  }
  ```

- **Resposta:**

  ```json
  {
      "message": "OK"
  }
  ```

### 3. **Remover uma Pessoa**

- **Método:** `DELETE`
- **URL:** `/pessoas/{idPessoa}`
- **Descrição:** Remove um registro de pessoa existente.
- **Resposta:**

  ```json
  {
      "message": "OK"
  }
  ```

### 4. **Obter Todas as Pessoas**

- **Método:** `GET`
- **URL:** `/pessoas`
- **Descrição:** Retorna uma lista de todas as pessoas.
- **Resposta:**

  ```json
  [
      {
          "idPessoa": 1,
          "nome": "João Silva",
          "dataNascimento": "1980-01-01",
          "salario": 5000.00,
          "observacoes": "PJ",
          "nomeMae": "Maria Silva",
          "nomePai": "José Silva",
          "cpf": "12345678900"
      }
  ]
  ```

### 5. **Obter uma Pessoa Específica**

- **Método:** `GET`
- **URL:** `/pessoas/{idPessoa}`
- **Descrição:** Retorna os detalhes de uma pessoa específica.
- **Resposta:**

  ```json
  {
      "idPessoa": 1,
      "nome": "João Silva",
      "dataNascimento": "1980-01-01",
      "salario": 5000.00,
      "observacoes": "PJ",
      "nomeMae": "Maria Silva",
      "nomePai": "José Silva",
      "cpf": "12345678900"
  }
  ```

## 🧪 Testando com Postman

1. **Importe as Requests:** Baixe e importe o [arquivo de coleção do Postman](./api-registro-pessoas.postman_collection.json) para testar as rotas.
