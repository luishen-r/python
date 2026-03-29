vel = int(input('Qual a velocidade do carro? '))
lim = int(vel-80)*7
if vel > 80:
    print('MULTADO! Você está excedendo os limites de velocidade de 80km/h')
    print(f'Sua multa está avaliada em R${lim}')
else:
    print('Tenha um ótimo dia!')
