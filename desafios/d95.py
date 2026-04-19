jogador = dict()
time = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()

    for i in range(partidas):
        gol = int(input(f'    Quantos gols na partida {i+1}? '))
        gols.append(gol)

    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Digite novamente')
        else:
            break
    if resp == 'N':
        break

print('-='*30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<10} ', end='')
print()
print('-='*30)

for i, j in enumerate(time):
    print(f'{i+1:>3}. ', end='')
    for d in j.values():
        print(f'{str(d):<10} ', end='')
    print()

print('-='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (0 para parar) '))
    if busca == 0:
        print('Finalizando...')
        break
    if busca <= len(time):
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca-1]["nome"].upper()}:')
        for i, g in enumerate(time[busca-1]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    else:
        print(f'ERRO! Não existe jogador com código {busca}! Tente novamente.')
