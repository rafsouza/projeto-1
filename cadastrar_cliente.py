import sqlite3
import tkinter as tk

import pandas as pd

janela.title('Cadastro de Clientes')
janela.geometry("330x350")


def cadastrar_cliente():
    conexao = sqlite3.connect('banco_cliente.db')
    c = conexao.cursor()

    c.execute("INSERT INTO cliente VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })


    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

def exporta_clientes():
    conexao = sqlite3.connect('cliente.db')
    c = conexao.cursor()

    c.execute("SELECT *, oid FROM cliente.py")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['cpf','nome','sobrenome','email','telefone','Id_banco'])
    clientes_cadastrados.to_excel('cliente.xlsx')

    conexao.commit()

    conexao.close()


label_nome = tk.Label(janela, text='CPF')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)


entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(janela, width =35)
entry_cpf.grid(row=4, column=1, padx=10, pady=10)




botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)



botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela.mainloop()
