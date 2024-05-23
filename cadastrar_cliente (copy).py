import sqlite3

# Conectar ao banco de dados (se não existir, será criado)
conexao = sqlite3.connect('dados_clientes.db')

# Criar uma tabela chamada "clientes" com os campos nome, sobrenome, email e telefone
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    )
''')

# Função para inserir um novo cliente
def inserir_cliente(nome, sobrenome, email, telefone=None):
    cursor.execute('''
        INSERT INTO clientes (nome, sobrenome, email, telefone)
        VALUES (?, ?, ?, ?)
    ''', (nome, sobrenome, email, telefone))
    conexao.commit()
    print("Cliente inserido com sucesso!")

# Exemplo de inserção de um cliente
inserir_cliente("João", "Silva", "joao@example.com", "123456789")

# Fechar a conexão com o banco de dados quando terminar
conexao.close()
