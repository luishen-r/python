num = list()
numpar = []
numimpar= []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
    match r:
        case 'N':
            break
        case 'S':
            continue
        case _:
            while r not in 'SN':
                print('Respota Inválida')
                r = str(input('Quer continuar?[S/N] ')).strip().upper()
print(f'A lista formada foi {num}')
print(f'Os números pares dessa lista são {numpar}')
print(f'Os números impares dessa lista foram {numimpar}')