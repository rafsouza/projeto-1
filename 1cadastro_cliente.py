import customtkinter
import sqlite3

# Função para criar a tabela de clientes
def criar_tabela_clientes():
    # Conectar ao banco de dados
    banco = sqlite3.connect('1banco_cliente.db')
    cursor = banco.cursor()

    # Criar a tabela se ela ainda não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        sobrenome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT
                    )''')

    # Confirmar a criação da tabela e fechar a conexão com o banco de dados
    banco.commit()
    banco.close()

    print("Tabela 'clientes' criada com sucesso!")

# Função do botão [Enviar]
def cadastrar_cliente(nome, sobrenome, email, telefone):
    # Conectar ao banco de dados
    banco = sqlite3.connect('1banco_cliente.db')
    cursor = banco.cursor()

    # Inserir os dados do cliente na tabela
    cursor.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)",
                   (nome, sobrenome, email, telefone))

    # Confirmar a inserção e fechar a conexão com o banco de dados
    banco.commit()
    banco.close()

    print("Cliente cadastrado com sucesso!")

# Criar a tabela de clientes ao iniciar o programa
criar_tabela_clientes()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Coletivo Morro das Panelas - Cadastro de cliente")

texto = customtkinter.CTkLabel(janela, text="Cadastro de clientes")
texto.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text="Nome*", width=250)
nome.pack(padx=10, pady=10)

sobrenome = customtkinter.CTkEntry(janela, placeholder_text="Sobrenome*", width=250)
sobrenome.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Email*", width=250)
email.pack(padx=10, pady=10)

telefone = customtkinter.CTkEntry(janela, placeholder_text="Telefone", width=250)
telefone.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Cadastrar",  command=lambda: cadastrar_cliente(nome.get(), sobrenome.get(), email.get(), telefone.get()))  
botao.pack(padx=10, pady=10)

janela.mainloop()

# Conectar ao banco de dados
conexao = sqlite3.connect('1banco_cliente.db')

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Executar a consulta SQL
cursor.execute("SELECT * FROM clientes")

# Recuperar os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão com o banco de dados
conexao.close()
