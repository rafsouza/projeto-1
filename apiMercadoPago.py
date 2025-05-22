import mercadopago

# sdk = mercadopago.SDK("TOKEN DO MERCADOPAGO")
sdk = mercadopago.SDK("APP_USR-2857599939759343-051710-1361a8a0d6110ae7ca84b4bea2a5804d-2442488513")

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
            "pending": "https://127.0.0.1:5000/loja/compra/erro",
            "failure": "https://127.0.0.1:5000/loja/compra/erro"
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    # print(payment)
    return payment["init_point"]
