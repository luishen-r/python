times = ('Palmeiras', 'Flamengo', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza',
         'Goiás', 'Vasco', 'Bragantino', 'Botafogo', 'Ceará', 'Atlético-GO', 'Coritiba', 'Santos', 'Avaí', 'Juventude', 'Cuiabá',)
pos = times.index('Fortaleza')
for p, t in enumerate(times):
    print(p+1, t)
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'O Fortaleza está na posicão {pos+1}')
