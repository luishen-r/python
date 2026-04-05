print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
valt = valor
ced = 50
totced = 0
while True:
    if valt >= ced:
        valt -=ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        if valt == 0:
            break
print('VOLTE SEMPRE!')