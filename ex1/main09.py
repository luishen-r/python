r = 'S'
par = impar = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    r = str(input('Quer continuar?[S/N] ')).upper().strip()
print(f'A quantidade de pares foi {par}, e a quantidade de ímpares foi {impar}')