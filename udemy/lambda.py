lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista.sort(key=lambda item: item['nome'])
for itens in lista:
    for k, v in itens.items():
        print(f'{k}: {v}')
        

def executa(function, *args):
    return function(*args)


print(
    executa(
        lambda x, y: x + y, 20, 10
            )
)