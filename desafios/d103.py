def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


name = str(input('Nome do jogador: ')).strip()
goals = str(input('Número de gols: ')).strip()
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name == '':
    ficha(gols=goals)
else:
    ficha(name, goals)