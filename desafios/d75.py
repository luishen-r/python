num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 aparece na posção {num.index(3)+1}')
print('Os valores pares são eles ', end='')
for n in num:
    if n % 2 == 0:
        print(n)