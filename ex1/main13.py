def título(txt):
    print('-' * 30)
    print(txt.center(30))
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é igual a {s}')


def lin():
    print('-' * 30)


def contador(*num):
    print(f'Recebi os valores {num} e são ao todo {len(num)} números.')


def dobro(list):
    for c in range(0, len(list)):
        list[c] *= 2
    print(f'O dobro dos valores é {list}')


título('Funções')
soma(4, 5)
lin()
valores = [7, 2, 5, 0, 4]
contador(*valores)
dobro(valores)
