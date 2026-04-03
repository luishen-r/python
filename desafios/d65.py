r = 'S'
cont = 0
s = 0 
while r == 'S':
    n = int(input('Digite um número: '))
    s += n
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    r = input('Deseja continuar? [S/N] ').upper().strip()[0]
print(f'Você digitou {cont} números e a média entre eles foi {s/cont:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor}')

    