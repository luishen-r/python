dist = int(input('Qual a distância de sua viagem? '))
if dist <= 200:
    print(f'O valor cobrado pela sua passagem será de {dist*0.5}')
else:
    print(f'O valor cobrado pela sua viagem será de {dist*0.45}')
