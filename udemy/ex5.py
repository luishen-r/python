from copy import deepcopy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [{**p ,'preco': round(p['preco'] *1.1, 2)} for p in deepcopy(produtos)]
print(novos_produtos)

ordenados = sorted(
    deepcopy(novos_produtos),
    key=lambda p: p['preco'], reverse=True
)

print(ordenados)



