# Arquivo com as rotas relacionadas Loja virtual
import os

from flask import Blueprint, redirect, render_template, request, url_for, flash, session
# from xlsxwriter import Workbook
from lojacoletivo import db, bcrypt
from lojacoletivo.models import Produto, Cliente, Pedido, Itens_Pedido
from random import randint
from apiMercadoPago import gerar_link_pagamento

bp_loja = Blueprint('/loja', __name__, template_folder='templates')

pp = 12 # per_pag das paginações

# Função para buscar as categorias, usada para a navbar 
def cats():
  cats = Produto.query.with_entities(Produto.categoria, Produto.id).group_by(Produto.categoria).distinct() # Gera tuplas (categoria, id); 
  return cats

# Buscar categorias
@bp_loja.route('/qcat/<int:id>')#, methods=['GET', 'POST'])
def get_cat(id):
  pag=request.args.get('pag',1,type=int)
  p = Produto.query.get(id) # Com paginação
  qcat = Produto.query.filter_by(categoria=p.categoria).paginate(page=pag,per_page=pp) # Com paginação
  #  p = Produto.query.get(id) # Sem paginação
  # qcat = Produto.query.filter_by(categoria=p.categoria).all() # Sem paginação
  #  print('Produto: ', str(p.nome_produto),' | ', str(p.categoria))
  return render_template('/loja/produtos/produto_main.html', title= 'Categoria:'+str(p.categoria)+' - Morro das Panelas', qcat=qcat, categorias=cats(), id=id)



# Acessar página principal da loja
@bp_loja.route('/', methods=['GET', 'POST']) # futuramente vai ser a main ( / )do site
def loja_main():
  if request.method == 'GET':
    pag=request.args.get('pag',1,type=int)
    pd = Produto.query.order_by(Produto.nome_produto.asc()).paginate(page=pag,per_page=pp) # Com paginação
    # pd = Produto.query.order_by(Produto.nome_produto.asc()).all() # Sem paginação
    return render_template('/loja/produtos/produto_main.html', title= 'Loja - Morro das Panelas', pd=pd, categorias=cats())
  
  
# Acessar página individual de um produto
@bp_loja.route('/<int:id>', methods=['GET', 'POST'])
def produto_individual(id):
  pd = Produto.query.get(id)
  # print(pd.nome_produto)

  if request.method == 'GET':
    return render_template('/loja/produtos/produto_individual.html', title= str(pd.nome_produto)+' - Morro das Panelas', pd=pd, categorias=cats())
  

# Resetar seção
@bp_loja.route('/resetar')
def EmptySession():
    try:
        session.clear()
        print('Sessão resetada')
        return redirect(url_for('home'))
    except Exception as e:
        print(e) 


# Finalizar compra
'''@bp_loja.route('/confirmar_pedido', methods=['GET', 'POST']) # futuramente vai ser a main ( / )do site
def confirmar_pedido():
  if 'email' not in session:
      return redirect('/loja/cliente/login')
  
  id=session['email']
  cl = Cliente.query.filter_by(email=id).first()
  carrinho = session.get('CarrinhoLoja', {})

  obs = request.form.get('obs')
  print ('Obs (Loja): ',obs)
  ## Fazer checkout - 1 etapa
  ## Pegar info do admin e enviar solicitação para API do mercadopago

  link_iniciar_pagamento = gerar_link_pagamento(carrinho)

  if request.method == 'GET':
    tot=0
    for key, p in session['CarrinhoLoja'].items():
      tot = sum(float(p['preco']) * float(p['qtd']) for p in carrinho.values())
    return render_template('/loja/produtos/confirmar.html', title= 'Pedido Realizado - Morro das Panelas', cl=cl, categorias=cats(), obs=obs,
                            tot=tot, link_pagamento=link_iniciar_pagamento)'''


## Receber e processar resposta da API - 2 etapa 
## Persistir 
@bp_loja.route('/compra/sucesso')
def compra_sucesso():
  # if request.method == 'POST':
    if 'email' not in session:
      return redirect('/loja/cliente/login')
    
    id=session['email']
    cl = Cliente.query.filter_by(email=id).first()

    # Coleta de argumentos da compra
    cstatus=request.args.get('status') # Status da compra (não confundir com o do pedido)
    payment_id=request.args.get('payment_id')
    preference_id=request.args.get('preference_id') # ID da compra no mercado pago
    payment_type=request.args.get('payment_type')
    npd = session['NumeroPedido']
    ped = Pedido.query.get(npd)
    
    # limpar Numero de pedido atual
    try:
        session.pop('NumeroPedido',None)
    except Exception as e:
        print(e)
    ped.preference_id = preference_id
    ped.payment_id = payment_id
    db.session.add(ped)
    db.session.commit() # Registra dados do pagamento
    
    print('Status: ', cstatus)
    # print('Teste npd - ', session['NumeroPedido'])


    '''# Gera número do pedido
    # obs = request.form.get('obs')
    npd = randint(10000000, 99999999) # Número de pedido aleatório que não esteja no banco de dados
    while Pedido.query.filter_by(N_pedido=npd).first() != None:
      npd = randint(10000000, 99999999)
  
  
    # Para o pedido: id(cliente), npd, obs
    ped = Pedido(cl.id, npd, obs) # id = cliente_id
    # qtd = [a.replace(',','.') for a in qtd] # Substituir vírgula por ponto
    db.session.add(ped)
    db.session.commit() # Registra o pedido (por enquanto sem itens)
  
    # Para cada item do pedido (laço): npd, str(nome[a])+' ('+str(porcao[a])+')', pr_id[a], preco[a], qtd[a]
    for key, p in session['CarrinhoLoja'].items():
      it = Itens_Pedido(npd,str(p['nome'])+' ('+str(p['porcao'])+')',key,str(p['preco']),str(p['qtd']))
      db.session.add(it)
      db.session.commit() # Registra os itens do pedido
  
    # Atualizar estoque
    print('Pedido ',npd,' : Compra efetuada, estado = Em separação')
    it = Itens_Pedido.query.filter_by(N_pedido=npd)
    for i in it:
      it_pd =Produto.query.get(i.produto_id)
      it_pd.qtd = it_pd.qtd - i.qtd # Remove do estoque
      # print('(-) Estoque de',it_pd.nome_produto,'de ',it_pd.qtd + i.qtd,' para ',it_pd.qtd) # pr
      db.session.add(it_pd)
      db.session.commit()
    ped.status="Em separação"
    db.session.add(ped)
    db.session.commit() # Registra o pedido (por enquanto sem itens)
  
    # limpar carrinho
    try:
        session.pop('CarrinhoLoja',None)
    except Exception as e:
        print(e)'''
  
    # print('Pedido ',npd,' finalizado com sucesso!')
    return render_template('/loja/produtos/tela_pagamento.html', title= 'Finalizar Pedido - Morro das Panelas', categorias=cats(), n=npd, 
                           cstatus='approved', payment_id=payment_id, preference_id=preference_id, payment_type=payment_type)
  
  # print('Estado: ',request.args.get('status'))
  # print('ID pagamento: ',request.args.get('payment_id'))
  # print('ID compra: ',request.args.get('preference_id'))
  # return render_template('/loja/compra_status.html', status='success', mensagem='Pagamento confirmado com sucesso!')

@bp_loja.route('/compra/pendente')
def compra_pendente():
    return render_template('/loja/compra_status.html', cstatus='pending', mensagem='Seu pagamento está pendente. Aguarde a confirmação.')

@bp_loja.route('/compra/erro')
def compra_erro():
    cstatus=request.args.get('status') # Status da compra (não confundir com o do pedido)
    # payment_id=request.args.get('payment_id')
    preference_id=request.args.get('preference_id') # ID da compra no mercado pago
    # payment_type=request.args.get('payment_type')
    return render_template('/loja/produtos/tela_pagamento.html', title= 'Finalizar Pedido - Morro das Panelas', categorias=cats(),
                           cstatus='failure', preference_id=preference_id)
    # return render_template('/loja/compra_status.html', status='failure', mensagem='Houve um erro no pagamento. Tente novamente.')


'''https://127.0.0.1:5000/loja/compra/sucesso?
collection_id=111488349659
collection_status=approved
payment_id=111488349659
status=approved&external_reference=null
payment_type=account_money
merchant_order_id=31082427425
preference_id=2442488513-401c56bc-046e-4cbb-bd53-6654a6780310
site_id=MLB
processing_mode=aggregator
merchant_account_id=null'''

'''https://127.0.0.1:5000/loja/compra/sucesso?
collection_id=111509365357
collection_status=approved
payment_id=111509365357
status=approved
external_reference=null
payment_type=credit_card
merchant_order_id=31087233191
preference_id=2442488513-2106f18f-3a53-4967-9192-d1ed8d45f35c
site_id=MLB
processing_mode=aggregator
merchant_account_id=null'''
