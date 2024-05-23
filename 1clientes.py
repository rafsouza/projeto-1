import sqlite3
import customtkinter

def exibir_clientes():
    # Conexão com o banco de dados
    conn = sqlite3.connect('1banco_cliente.db')
    c = conn.cursor()

    # Recuperar os clientes do banco de dados
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()

    # Fechar conexão com o banco de dados
    conn.close()

    # Criar nova janela para exibir os clientes
    janela_clientes = customtkinter.CTk()
    janela_clientes.geometry("400x600")
    janela_clientes.title("Lista de Clientes")

    # Exibir os clientes na nova janela
    texto = customtkinter.CTkLabel(janela_clientes, text="Lista de Clientes")
    texto.pack(padx=10, pady=10)

    for cliente in clientes:
        # Cada cliente será exibido em uma linha
        texto_cliente = customtkinter.CTkLabel(janela_clientes, text=cliente)
        texto_cliente.pack(padx=10, pady=5)

    janela_clientes.mainloop()

# Função principal para exibir os clientes
def codcliente():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela = customtkinter.CTk()
    janela.geometry("400x600")
    janela.title("Coletivo Morro das Panelas - Lista de Clientes")

    texto = customtkinter.CTkLabel(janela, text="Lista de Clientes")
    texto.pack(padx=10, pady=10)

    # Botão para exibir os clientes
    botao_exibir = customtkinter.CTkButton(janela, text="Exibir Clientes", command=exibir_clientes)
    botao_exibir.pack(padx=10, pady=10)

    janela.mainloop()

# Função para cadastrar clientes
def cadastrar_cliente(nome, sobrenome, email, telefone):
    # Conexão com o banco de dados
    conn = sqlite3.connect('1banco_cliente.db')
    c = conn.cursor()

    # Inserir os dados do cliente na tabela
    c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)", (nome, sobrenome, email, telefone))

    # Confirmar a inserção e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

    print("Cliente cadastrado com sucesso!")

# Interface para cadastrar clientes
def cadastro_cliente():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela = customtkinter.CTk()
    janela.geometry("400x600")
    janela.title("Coletivo Morro das Panelas - Cadastro de Cliente")

    texto = customtkinter.CTkLabel(janela, text="Cadastro de Cliente")
    texto.pack(padx=10, pady=10)

    nome = customtkinter.CTkEntry(janela, placeholder_text="Nome", width=250)
    nome.pack(padx=10, pady=10)

    sobrenome = customtkinter.CTkEntry(janela, placeholder_text="Sobrenome", width=250)
    sobrenome.pack(padx=10, pady=10)

    email = customtkinter.CTkEntry(janela, placeholder_text="Email", width=250)
    email.pack(padx=10, pady=10)

    telefone = customtkinter.CTkEntry(janela, placeholder_text="Telefone", width=250)
    telefone.pack(padx=10, pady=10)

    # Botão para cadastrar o cliente
    botao_cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=lambda: cadastrar_cliente(nome.get(), sobrenome.get(), email.get(), telefone.get()))
    botao_cadastrar.pack(padx=10, pady=10)

    janela.mainloop()

codcliente()  # Chama a função para exibir os clientes
