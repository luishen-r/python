a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
t = a1 + (10-1)*r
for c in range(a1, t+1, r):
    print(f'{c}', end="->")
print('FIM!')
