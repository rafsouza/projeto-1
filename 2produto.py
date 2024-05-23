import sqlite3
import customtkinter

def exibir_produtos():
    # Conexão com o banco de dados
    conn = sqlite3.connect('2banco_produto.db')
                          
    c = conn.cursor()

    # Recuperar os produtos do banco de dados
    c.execute("SELECT * FROM produtos")
    produtos = c.fetchall()

    # Fechar conexão com o banco de dados
    conn.close()

    # Criar nova janela para exibir os produtos
    janela_produtos = customtkinter.CTk()
    janela_produtos.geometry("400x600")
    janela_produtos.title("Lista de Produtos")

    # Exibir os produtos na nova janela
    texto = customtkinter.CTkLabel(janela_produtos, text="Lista de Produtos")
    texto.pack(padx=10, pady=10)

    for produto in produtos:
        # Cada produto será exibido em uma linha
        texto_produto = customtkinter.CTkLabel(janela_produtos, text=produto)
        texto_produto.pack(padx=10, pady=5)

    janela_produtos.mainloop()

# Função principal para exibir os produtos
def codproduto():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela = customtkinter.CTk()
    janela.geometry("400x600")
    janela.title("Coletivo Morro das Panelas - Lista de Produtos")

    texto = customtkinter.CTkLabel(janela, text="Lista de Produtos")
    texto.pack(padx=10, pady=10)


    # Botão para exibir os produtos
    botao_exibir = customtkinter.CTkButton(janela, text="Exibir Produtos", command=exibir_produtos)
    botao_exibir.pack(padx=10, pady=10)

    janela.mainloop()

# Função do botão [Enviar]
def clique3():
    print("Enviou")

codproduto()
