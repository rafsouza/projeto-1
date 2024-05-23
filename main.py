#Versão V02

# Bibliotecas
import customtkinter
from vercadastro import prodcadastro, produtocadastro
from janela import codjanela
from criacadastro import codcadastr, codcliente, codproduto
import pandas as pd
import sqlite3



# Funções dos cliques

def cadprodutor():
  print("Acessando Cadastro Produtores")
  codcadastr()

def cadcliente():
  print("Acessando Cadastro Clientes")
  codcliente()

def cadproduto():
  print("Acessando Inclusão de Produtos")
  codproduto()

def verprodutor():
  print("Acessando Produtores registrados")
  prodcadastro()

def verproduto():
  print("Acessando visualização de Produtos")
  produtocadastro()

# Configurações das janelas do customkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Seção de login

#codjanela()

if 1: #Colocar aqui a condição de Login valida


  
  # Seção de seleção de opções
  janela = customtkinter.CTk()
  janela.geometry("650x500")
  janela.title("Coletivo Morro das Panelas")

  texto = customtkinter.CTkLabel(janela, text="Escolha a opção desejada:")
  texto.pack(padx=10, pady=10)

  botao1 = customtkinter.CTkButton(janela, text="Cadastrar Produtor",  command=cadprodutor)
  botao1.pack(padx=10, pady=10)

  botao2 = customtkinter.CTkButton(janela, text="Ver Produtores",  command=verprodutor)
  botao2.pack(padx=10, pady=10)

  botao3 = customtkinter.CTkButton(janela, text="Cadastrar Cliente",  command=cadcliente)
  botao3.pack(padx=10, pady=10)

  botao4 = customtkinter.CTkButton(janela, text="Adicionar Produtos",  command=cadproduto)
  botao4.pack(padx=10, pady=10)

  botao5 = customtkinter.CTkButton(janela, text="Ver Produtos",  command=verproduto)
  botao5.pack(padx=10, pady=10)

  janela.mainloop()

#  Fim V02



# Versão V01
'''from janela import codjanela

codjanela()
'''
# Fim V01



# Versão V00
'''import customtkinter

def clique():
  print("Funciona")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Coletivo Morro das Panelas")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu Email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text= "Digite sua Senha", show="#")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Clique para Entrar",  command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
'''
# Fim V00

#visualização do BQ
