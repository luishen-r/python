from math import factorial
n = int(input('Digite um número para saber seu fatorial:'))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} x ' if c > 1 else f'{c} = ', end='')
    c -= 1
print(factorial(n))
