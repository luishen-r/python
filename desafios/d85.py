num = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i} número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Os números pares foram {num[0]}')
print(f'Os números ímpares foram {num[1]}')
