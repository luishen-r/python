s = 0
for c in range (1, 51):
    n = c
    if n % 2 ==0:
        print(c)
    s += n
print(f'O somatório desse números é {s}')