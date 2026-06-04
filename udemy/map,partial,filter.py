from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def porcentagem(v, p):
    return round(v * p, 2)

aumentar_dez_porcento = partial(
    porcentagem,
    p = 1.5
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos

novos_prod = map(
    lambda p: {**p, 'preco': round(p['preco'] * 1.5, 2)},
    produtos 
)

print_iter(novos_prod)