from flask import jsonify
from ..config import Config
import psycopg2

def get_db_connection():
    return psycopg2.connect(Config.DATABASE_URL)

def create_pessoa(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.callproc('inserir_pessoa', (
        data['nome'],
        data['dataNascimento'],
        data['salario'],
        data['observacoes'],
        data['nomeMae'],
        data['nomePai'],
        data['cpf']
    ))
    idPessoa = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'idPessoa': idPessoa}), 201

def update_pessoa(idPessoa, data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.callproc('atualizar_pessoa', (
        idPessoa,
        data['nome'],
        data['dataNascimento'],
        data['salario'],
        data['observacoes'],
        data['nomeMae'],
        data['nomePai'],
        data['cpf']
    ))
    result = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': result})

def delete_pessoa(idPessoa):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.callproc('remover_pessoa', (idPessoa,))
    result = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': result})

def get_all_pessoas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.callproc('selecionar_todos_registros')
    pessoas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pessoas)

def get_pessoa(idPessoa):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.callproc('selecionar_registro', (idPessoa,))
    pessoa = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(pessoa)
