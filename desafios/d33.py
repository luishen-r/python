a = int(input('Digitte um valor qualquer: '))
b = int(input('Digitte um valor qualquer: '))
c = int(input('Digitte um valor qualquer: '))
menor = a
if a > b and c > b:
    menor = b
if a > c and b > c:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
