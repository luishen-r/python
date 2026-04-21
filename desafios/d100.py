from random import randint, shuffle


def sorteio(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    shuffle(lista)
    print(f'Os números sorteados foram: {lista}')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares é {soma}.')


n = list()
sorteio(n)
somaPar(n)
