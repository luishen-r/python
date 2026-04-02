from time import sleep
from random import randint
jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'{"Vamos jogar Jokenpô!":=^40}')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(f'O jogador escolheu {jogadas[jogador]}')
print(f'O computador escolheu {jogadas[computador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')

