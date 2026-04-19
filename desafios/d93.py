jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()

for i in range(partidas):
    gol = int(input(f'    Quantos gols na partida {i+1}? '))
    gols.append(gol)

jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for i in range(partidas):
    print(f'     =>Na partida {i+1}, fez {gols[i]} gols')
print(f'Foi um total de {jogador["total"]} gols')
