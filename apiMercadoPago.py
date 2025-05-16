import mercadopago

sdk = mercadopago.SDK("TOKEN DO MERCADOPAGO")

def gerar_link_pagamento(carrinho):
    items = []
    for key, p in carrinho.items():
        item = {
            "id": str(p['produto_id']),
            "title": p['nome'],
            "description": f"{p['nome']} ({p['porcao']})",
            "quantity": int(p['qtd']),
            "currency_id": "BRL",
            "unit_price": float(p['preco'])
        }
        items.append(item)

    payment_data = {
        "items": items,
        "back_urls": {
            "success": "https://127.0.0.1:5000/loja/compra/sucesso",
            "pending": "https://127.0.0.1:5000/loja/compra/pendente",
            "failure": "https://127.0.0.1:5000/loja/compra/erro"
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    return payment["init_point"]
