s = 0
c = 0
for p in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 ==0:
        s += n
        c += 1
print(f'A soma dos números pares, sendo eles {c} valores, informados é {s}')
