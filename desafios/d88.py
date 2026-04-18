from random import shuffle
from time import sleep

print('-' * 30)
print(f'{"JOGO DA MEGASENA":^30}')
print('-' * 30)

n = int(input('Quantos jogos você quer que eu sorteie? '))

if n > 10:
    print('Não é possível gerar mais de 10 jogos sem repetir números.')
else:
    numeros = list(range(1, 61))
    shuffle(numeros)

    for i in range(n):
        jogo = numeros[i*6:(i+1)*6] 
        jogo.sort()
        print(f'Jogo {i+1}: {jogo}')
        sleep(1.5)

print('-' * 30)
print(f'{"BOA SORTE!":^30}')
print('-' * 30)