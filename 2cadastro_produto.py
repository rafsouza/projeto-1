#cadastrar produto
import customtkinter
import sqlite3

# Função para criar a tabela de produtos
def criar_tabela():
    # Conectar ao banco de dados
    banco = sqlite3.connect('2banco_produto.db')
    cursor = banco.cursor()

    # Criar a tabela se ela ainda não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        quantidade INTEGER,
                        porcao TEXT,
                        preco REAL,
                        categoria TEXT
                    )''')

    # Confirmar a criação da tabela e fechar a conexão com o banco de dados
    banco.commit()
    banco.close()

    print("Tabela 'produtos' criada com sucesso!")

# Função do botão [Enviar]
def clique3(nome_produto, quantidade, porcao, preco_produto, categoria):
    # Conectar ao banco de dados
    banco = sqlite3.connect('2banco_produto.db')
    cursor = banco.cursor()

    # Inserir os dados do produto na tabela
    cursor.execute("INSERT INTO produtos (nome, quantidade, porcao, preco, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nome_produto, quantidade, porcao, preco_produto, categoria))

    # Confirmar a inserção e fechar a conexão com o banco de dados
    banco.commit()
    banco.close()

    # Limpar os campos após o envio
    nome.delete(0, 'end')
    qtd.delete(0, 'end')
    prc.delete(0, 'end')
    preco.delete(0, 'end')
    categ.delete(0, 'end')

    print("Produto cadastrado com sucesso!")

# Criar a tabela ao iniciar o programa
criar_tabela()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Coletivo Morro das Panelas - Cadastro de produto")

texto = customtkinter.CTkLabel(janela, text="Cadastro de produtos")
texto.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text="Nome do produto*", width=250)
nome.pack(padx=10, pady=10)

qtd = customtkinter.CTkEntry(janela, placeholder_text="Quantidade*", width=250)
qtd.pack(padx=10, pady=10)

prc = customtkinter.CTkEntry(janela, placeholder_text="Porção (unidade, dúzia, kg, ml, ...)*", width=250)
prc.pack(padx=10, pady=10)

preco = customtkinter.CTkEntry(janela, placeholder_text="Preço (por porção)", width=250)
preco.pack(padx=10, pady=10)

categ = customtkinter.CTkEntry(janela, placeholder_text="Categoria", width=250)
categ.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Enviar",  command=lambda: clique3(nome.get(), qtd.get(), prc.get(), preco.get(), categ.get()))  
botao.pack(padx=10, pady=10)

janela.mainloop()

import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('2banco_produto.db')

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Executar a consulta SQL
cursor.execute("SELECT * FROM produtos")

# Recuperar os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão com o banco de dados
conexao.close()
