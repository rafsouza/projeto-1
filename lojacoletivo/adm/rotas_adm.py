# Arquivo com as rotas relacionadas administração
import os

from flask import Blueprint, redirect, render_template, request, session
# from xlsxwriter import Workbook
from lojacoletivo import db, bcrypt, app
from lojacoletivo.models import Admin
# from models import Produto
from .formulario import RegistraFormulario, LoginFormulario

bp_adm = Blueprint('adm', __name__, template_folder='templates')

# Acessar página principal de administração
@bp_adm.route('/home', methods=['GET', 'POST'])
def adm_home():
  if request.method == 'GET':
    if 'email_adm' not in session:
     return redirect('/adm/login_adm')
    else:      
     return render_template('adm/home_adm.html', title= 'Administração - Morro das Panelas')

 
# Login de administrador
@bp_adm.route('/login_adm', methods=['GET', 'POST'])
def login_adm():
  form=LoginFormulario(request.form)
  if request.method == 'GET':
    return render_template('adm/login_adm.html', title= 'Login - Morro das Panelas', form=form)

  if request.method == 'POST':
    if form.validate():
      administrador = Admin.query.filter_by(email_adm=form.email_adm.data).first()
      if administrador and bcrypt.check_password_hash(administrador.senha, form.senha.data): # 
        print('Login efetuado em: '+str(form.email_adm.data))
        session['email_adm'] = form.email_adm.data # necessita do app.secret_key para funcionar
        return redirect('/adm/home')
      else:
        print('Usuário ou senha inválidos')
        return render_template('adm/login_adm.html', title= 'Login - Morro das Panelas', form=form, msg= 'Usuário ou senha inválidos')
    

# Cadastrar um administrador
@bp_adm.route('/create', methods=['GET', 'POST'])
def create():
  form=RegistraFormulario(request.form)
  if request.method == 'GET':
    return render_template('adm/adm_create.html', form=form, title='Cadastro de Administradores')

  if request.method == 'POST': 
    if form.validate():
      nome = request.form.get('nome')
      usuario_adm = request.form.get('usuario_adm')
      email_adm = request.form.get('email_adm')
      print(form.senha.data)
      hash_senha = bcrypt.generate_password_hash(form.senha.data) #senha encriptada #
      # print(hash_senha)

      adm = Admin(nome, usuario_adm, email_adm, hash_senha)
      db.session.add(adm)
      db.session.commit()
    else:
      print('Erro de validação: validators = '+str(form.validate()))
      return render_template('adm/adm_create.html', form=form, title='Cadastro de Administradores')

  #return 'Cadastro efetuado com sucesso!'
  # return redirect('/adm/registra/'+str(adm.usuario_adm))
  return redirect('/adm/read')


# Lista de administradores
@bp_adm.route('/read')
def read():
  if request.method == 'GET':
    if 'email_adm' not in session:
     return redirect('/adm/login_adm')
  adm = Admin.query.all()
  return render_template('adm/adm_read.html', title='Lista de Administradores cadastrados', adm=adm)


# Indice adm
@bp_adm.route('/index')
def index():
  if request.method == 'GET':
    if 'email_adm' not in session:
     return redirect('/adm/login_adm')
  return (render_template('adm/index_adm.html'))


# Fazer logout
@bp_adm.route('/logout')
def AdmLogout():
  try:
    session.pop('email_adm',None)
    # Esvaziar carrinho
    # print('Logout realizado com sucesso!')
    return redirect('/adm/home')
  except Exception as e:
      print(e) 
