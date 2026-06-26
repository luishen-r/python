campeonato = []

for i in range(12):
    print(f'\nTime {i + 1}')

    time = input('Nome do time: ')
    pontos = int(input('Pontos: '))
    jogos = int(input('Jogos: '))
    vitorias = int(input('Vitórias: '))
    empates = int(input('Empates: '))
    derrotas = int(input('Derrotas: '))

    campeonato.append([time, pontos, jogos, vitorias, empates, derrotas])
    
campeonato.sort(key=lambda x: x[2], reverse=True)

print('\n=== CLASSIFICAÇÃO FINAL ===')
for i, time in enumerate(campeonato, start=1):
    print(f'{i:2}º - {time[1]} ({time[2]} pts)')

print('\n=== CAMPEÃO BRASILEIRO ===')
print(f'{campeonato[0][1]} - {campeonato[0][2]} pontos')

print('\n=== CLASSIFICADOS PARA A LIBERTADORES ===')
for i in range(5):
    print(f'{i+1}º - {campeonato[i][1]}')

print('\n=== CLASSIFICADOS PARA A SUL-AMERICANA ===')
for i in range(5, 10):
    print(f'{i+1}º - {campeonato[i][1]}')

print('\n=== REBAIXADOS PARA A SÉRIE B ===')
for i in range(10, 12):
    print(f'{i+1}º - {campeonato[i][1]}')