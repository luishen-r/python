princ = []
mai = 0
men = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    princ.append([nome, peso])
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        print('FINALIZANDO...')
        break
pesos = [p[1] for p in princ]
mai = max(pesos)
men = min(pesos)
print(f'O maior peso foi {mai}. As pessoa com esse peso são: ', end='')
for nome, peso in princ:
    if peso == mai:
        print(f'{nome}')
print(f'O menor peso foi {men}. As pessoa com esse peso foram: ', end='')
for name, weight in princ:
    if weight == men:
        print(f'{name}')
