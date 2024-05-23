import tkinter as tk
from tkinter import messagebox
import sqlite3
import customtkinter

# Função para criar a tabela de usuários
def criar_tabela_usuarios():
    conn = sqlite3.connect('3usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (email TEXT PRIMARY KEY, senha TEXT)''')
    conn.commit()
    conn.close()

# Função para verificar se o usuário existe no banco de dados
def verificar_login(email, senha):
    conn = sqlite3.connect('3usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
    if cursor.fetchone() is not None:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Email ou senha incorretos.")
    conn.close()

# Função para cadastrar um novo usuário no banco de dados
def cadastrar_usuario(email, senha):
    conn = sqlite3.connect('3usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (email, senha))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Este email já está cadastrado.")
    conn.close()

# Função para o botão de login
def fazer_login():
    email_input = email.get()
    senha_input = senha.get()
    verificar_login(email_input, senha_input)

# Função para o botão de cadastrar usuário
def cadastrar():
    email_input = email.get()
    senha_input = senha.get()
    cadastrar_usuario(email_input, senha_input)

# Criar a tabela de usuários se ela não existir
criar_tabela_usuarios()

# Configurações de aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Criar a janela
login = customtkinter.CTk()
login.geometry("400x400")
login.title("Coletivo Morro das Panelas - Login")

# Criar os widgets
texto = customtkinter.CTkLabel(login, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(login, placeholder_text="Digite seu Email", width=250)
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(login, placeholder_text="Digite sua Senha", show="*", width=250)
senha.pack(padx=10, pady=10)

botao_login = customtkinter.CTkButton(login, text="Clique para Entrar", command=fazer_login)
botao_login.pack(padx=10, pady=10)

botao_cadastrar = customtkinter.CTkButton(login, text="Cadastrar Usuário", command=cadastrar)
botao_cadastrar.pack(padx=10, pady=10)

login.mainloop()
