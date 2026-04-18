matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
c3 = 0
p2 = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(
            input(f'Digite um valor para a posição ({l+1}, {c+1}) da matriz: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            c3 += matriz[l][c]
        if l == 1:
            p2 = max(matriz[l])
    print()
print(f'{pares}')
print(f'{c3}')
print(f'{p2}')
