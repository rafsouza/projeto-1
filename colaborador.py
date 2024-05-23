
import sql

conexao = sql.connect('colaboradores.db')

c = conexao.cursor()

c.execute("""CREATE TABLE  colaboradores (
    nome text,
     sobrenome text,
     email text,
     telefone text
)""")