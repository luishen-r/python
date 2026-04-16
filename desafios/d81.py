num = list()
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
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
reverso = sorted(num, reverse=True)
print('='*40)
print(f'Foram digitados {len(num)} valores')
print(f'A lista em ordem decrescente é {reverso}')
if 5 in num:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está presente na lista')
                