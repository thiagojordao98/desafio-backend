import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def test_db_connection():
    try:
        # Obter a URL de conexão do banco de dados da variável de ambiente
        DATABASE_URL = os.getenv('DATABASE_URL')
        
        # Conectar ao banco de dados usando DATABASE_URL
        conn = psycopg2.connect(DATABASE_URL)
        # Criar um cursor
        cur = conn.cursor()
        
        # Executar uma consulta simples
        cur.execute('SELECT version();')
        
        # Obter o resultado
        db_version = cur.fetchone()
        
        # Fechar o cursor e a conexão
        cur.close()
        conn.close()
        
        # Imprimir a versão do banco de dados
        print('Conexão bem-sucedida!')
        print('Versão do banco de dados:', db_version[0])
        
    except Exception as e:
        print('Erro ao conectar ao banco de dados:')
        print(e)

if __name__ == '__main__':
    test_db_connection()
