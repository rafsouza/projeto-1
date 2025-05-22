# Arquivo com as rotas relacionadas Loja virtual
from flask import Blueprint, redirect, render_template, request, url_for, flash, session, current_app
from lojacoletivo import db
from lojacoletivo.models import Produto, Pedido, Itens_Pedido, Cliente
from lojacoletivo.loja.rotas_loja import cats
from .formulario import OpcoesPagamento
from random import randint
from apiMercadoPago import gerar_link_pagamento

bp_carro = Blueprint('/carrinho', __name__, template_folder='templates')


# Função
def Mix_dict(dic1,dic2):
    # print('dic1 : ',str(type(dic1)),' | dic2 : ',str(type(dic2)))
    if isinstance(dic1,list) and isinstance(dic2,list):
        return dic1 + dic2
    elif isinstance(dic1,dict) and isinstance(dic2,dict): 
        # print('dict1 : ',dic1)
        # print('Lista dict1 : ',list(dic1.items()))
        # print('dict2 : ',dic2)
        # print('Lista dict2 : ',list(dic2.items()))
        # print('Resultado : ',dict(list(dic1.items()) + list(dic2.items())))
        return dict(list(dic1.items()) + list(dic2.items()))
    return False


# Adicionar itens no carrinho
@bp_carro.route('/addcart', methods=['POST'])
def addcart():
    try:
        prod_id=request.form.get('id')
        # print('ID: ',prod_id)
        qtd = request.form.get('qtd')
        # qtd = [a.replace(',','.') for a in qtd] # Substituir vírgula por ponto
        produto=Produto.query.filter_by(id=prod_id).first()
        # print('nome',produto.nome_produto)
        # print(produto)
        
        if id and qtd and request.method=='POST':
            dic_itens={prod_id:{'nome':produto.nome_produto, 'produto_id':produto.id, 'preco':produto.preco, 'qtd':qtd, 'qtmax':produto.qtd, 'porcao':produto.porcao, 'im_1':produto.im_1 }}
            # print('Compra: ',dic_itens)
            if 'CarrinhoLoja' in session:
                if prod_id in session['CarrinhoLoja']:
                    for key, it in session['CarrinhoLoja'].items():
                        if int(key) == int(prod_id):
                            session.modified = True
                            it['qtd']=str(int(it['qtd'])+1)
                            # print('Produto adicionado:  +1') # OK
                else:
                    session['CarrinhoLoja'] = Mix_dict(session['CarrinhoLoja'],dic_itens)
                    # print('Produto adcionado: Mix dicts') # Ok
                    return redirect(request.referrer) # fica na mesma página
            else:
                session['CarrinhoLoja']=dic_itens
                # print('Produto adicionado: Primeiro item') # OK
                return redirect(request.referrer)
            

    except Exception as e:
        print(e)
    finally:
        # print('Carrinho: ',session['CarrinhoLoja'].items())
        return redirect(request.referrer) 


# Ver itens do carrinho
@bp_carro.route('/', methods=['GET', 'POST'])
def vercart():
    if 'CarrinhoLoja' not in session or len(session['CarrinhoLoja'])<=0:
        print('O carrinho está vazio')
        # return redirect('/loja')
        return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas', msg = 'O carrinho está vazio', categorias=cats())

    if request.method == 'GET':
        # print('Carrinho total: ',session['CarrinhoLoja'].items())
        # subtot=0
        # form=OpcoesPagamento(request.form)
        tot=0
        for key, p in session['CarrinhoLoja'].items():
            tot += float(p['preco']) * float(p['qtd']) 
        tot = round(tot, 2) # deixar com 2 casas decimais
        # print('Carrinho: ',session['CarrinhoLoja'].items())
        return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas', categorias=cats(), tot =tot)#, form=form)

    if request.method == 'POST':
        if 'email' not in session:
            return redirect('/loja/cliente/login')
        id=session['email']
        cl = Cliente.query.filter_by(email=id).first()
        carrinho = session.get('CarrinhoLoja', {})

        obs = request.form.get('obs')
        # print ('Obs (Carrinho): ',obs)
        
        ### Gerar Pedido no banco de dados
        # Gera número do pedido
        npd = randint(10000000, 99999999) # Número de pedido aleatório que não esteja no banco de dados
        while Pedido.query.filter_by(N_pedido=npd).first() != None:
            npd = randint(10000000, 99999999)
    
        tot=0
        for key, p in session['CarrinhoLoja'].items():
            tot = sum(float(p['preco']) * float(p['qtd']) for p in carrinho.values())

        # Gerar Link do pagamento
        link_iniciar_pagamento = gerar_link_pagamento(carrinho)
    
        # Para o pedido: id(cliente), npd, obs
        ped = Pedido(cl.id, npd, obs) # id = cliente_id
        #### qtd = [a.replace(',','.') for a in qtd] # Substituir vírgula por ponto
        db.session.add(ped)
        db.session.commit() # Registra o pedido (por enquanto sem itens)
    
        # Para cada item do pedido (laço): npd, str(nome[a])+' ('+str(porcao[a])+')', pr_id[a], preco[a], qtd[a]
        for key, p in session['CarrinhoLoja'].items():
            it = Itens_Pedido(npd,str(p['nome'])+' ('+str(p['porcao'])+')',key,str(p['preco']),str(p['qtd']))
            db.session.add(it)
            db.session.commit() # Registra os itens do pedido
    
        # Atualizar estoque
        print('Pedido ',npd,' : Compra efetuada, estado = Em separação (aguardando pagamento)' )
        it = Itens_Pedido.query.filter_by(N_pedido=npd)
        for i in it:
            it_pd =Produto.query.get(i.produto_id)
            it_pd.qtd = it_pd.qtd - i.qtd # Remove do estoque
            # print('(-) Estoque de',it_pd.nome_produto,'de ',it_pd.qtd + i.qtd,' para ',it_pd.qtd) # pr
            db.session.add(it_pd)
            db.session.commit()
        ped.status="Em separação"
        ped.link=link_iniciar_pagamento
        db.session.add(ped)
        db.session.commit() # Registra o pedido (por enquanto sem itens)

        # Adicionar numero do pedido ne sessão (para ser pago)
        session['NumeroPedido']=str(npd)
        # print('Numero do pedido atual: ', session['NumeroPedido'])

            
        # limpar carrinho
        try:
            session.pop('CarrinhoLoja',None)
        except Exception as e:
            print(e)

        return render_template('/loja/produtos/confirmar.html', title= 'Pedido Realizado - Morro das Panelas', cl=cl, it=it, categorias=cats(), obs=obs,
                            tot=tot, link_pagamento=link_iniciar_pagamento)


# Esvaziar carrinho
@bp_carro.route('/esvaziar')
def esvaziar():
    try:
        session.pop('CarrinhoLoja',None)
        print('Carrinho esvaziado')
        return redirect('/loja')
    except Exception as e:
        print(e)
    return redirect(request.referrer)
    # return redirect('/loja')


# Atualizar itens do carrinho 
@bp_carro.route('/updatecart/<int:val>', methods=['POST'])
def updatecart(val):
    if 'CarrinhoLoja' not in session or len(session['CarrinhoLoja'])<=0:
        return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas', msg = 'O carrinho está vazio', categorias=cats())
    if request.method == 'POST':
         qtd = request.form.get('qtd')
        #  qtd = [a.replace(',','.') for a in qtd] # Substituir vírgula por ponto
         try:
             session.modified = True
             for key , it in session['CarrinhoLoja'].items():
                 if int(key) == val:
                    #  print('Antiga qtd: ',it['qtd'])
                     it['qtd'] = qtd
                    #  print('Nova qtd: ',it['qtd'])
            #  flash('Os itens do carrinho foram atualizados','success')
             tot=0
             for key, p in session['CarrinhoLoja'].items():
                tot += float(p['preco']) * float(p['qtd']) 
             return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas',
                                    msg = 'Os itens do carrinho foram atualizados', categorias=cats(), tot=tot)
         except Exception as e:
             print(e)
    return redirect(url_for('/carrinho.vercart'))
     

# Deletar itens do carrinho
@bp_carro.route('/delitem/<int:id>')
def delitem(id):
    if 'CarrinhoLoja' not in session or len(session['CarrinhoLoja'])<=0:
        return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas', msg = 'O carrinho está vazio', categorias=cats())
    try:
        session.modified = True
        for key , it in session['CarrinhoLoja'].items():
            if int(key) == id:
                # 
                session['CarrinhoLoja'].pop(key,None)
                print('Item removido')
                tot=0
                for key, p in session['CarrinhoLoja'].items():
                    tot += float(p['preco']) * float(p['qtd']) 
        return render_template('/loja/produtos/carrinho.html', title='Carrinho - Morro das Panelas', msg = 'Item removido do carrinho', categorias=cats(), tot=tot)
    except Exception as e:
        print(e)
    return redirect(url_for('/carrinho.vercart'))
