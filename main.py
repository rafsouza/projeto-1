#  Dependencias (instalação via terminal)
'''
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install Flask-Script
pip install python-dotenv

pip install xlsxwriter 

Criar um arquivo .flaskenv e inserir: FLASK_APP=main:app

Mais algumas abaixo 
'''

from flask import Flask, render_template
from flask_migrate import Migrate, migrate
#from flask_sqlalchemy import SQLAlchemy
from database import db
from produtores.rotas_produtores import bp_produtor
from produtos.rotas_produtos import bp_produto
from clientes.rotas_cliente import bp_cliente
from pedidos.rotas_pedidos import bp_pedido
from arquivos.op_arquivos import bp_arquivos

# Dados da conexão
app = Flask(__name__, static_url_path="/static")

# Configurando o banco de dados
conexao = 'sqlite:///banco.db'
app.config['SECRET-KEY'] = '7uyhX4regdg'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Precisa ficar em baixo do app.config para funcionar

# Registrando o blueprint
app.register_blueprint(bp_produtor, url_prefix='/produtor')
app.register_blueprint(bp_produto, url_prefix='/produto')
app.register_blueprint(bp_cliente, url_prefix='/cliente')
app.register_blueprint(bp_pedido, url_prefix='/pedidos')
app.register_blueprint(bp_arquivos, url_prefix='/arquivos')

# Associação do banco de dados com o aplicativo
migrate = Migrate(app, db)

# Códigos para criação do banco de dados (rodar via terminal, o primeiro só uma vez, os dois últimos a cada alteração do arquivo models.py)
'''
flask db init
flask db migrate -m "mensagem"
flask db upgrade

Caso apareça erro de  multiple heads, usar flask db merge heads -m "Mensagem" 
'''


# Rota principal
@app.route('/')
def home():
    #    return 'Hello from Flask!'
    return render_template('home.html', title='Coletivo Morro das Panelas')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
