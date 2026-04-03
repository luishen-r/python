from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 10...')
sleep(3)
n = randint(0, 10)
print('PENSEI')
acerto = False
tentativa = 0
while not acerto:
    jogador = int(input('Qual a sua jogada? '))
    if jogador == n:
        tentativa += 1
        acerto = True
        print('ACERTOU!')
    else:
        tentativa += 1
        acerto = acerto
        print('ERROU, tente denovo!')
print(f'Você precisou de {tentativa} chances para acertar')