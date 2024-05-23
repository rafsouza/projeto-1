import customtkinter
import sqlite3
from typing import text
import pandas

conexao = sqlite3.connect('banco_cliente.db')

c = conexao.cursor()

c.execute('''CREATE TABLE cliente (
cpf text,
nome text,
sobrenome text,
endereco text,
telefone text
)
''')

conexao.commit()

conexao.close()