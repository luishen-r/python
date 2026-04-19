from time import sleep
from random import randint

jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

for jogador, valor in jogo.items():
    print(f'{jogador} tirou {valor} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=lambda item:item[1], reverse=True)
print('Ranking dos jogadores:')
for i, jogador in enumerate(ranking):
    print(f'{i+1}º lugar: {jogador[0]} com {jogador[1]}')  