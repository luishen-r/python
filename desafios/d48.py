s = 0
i = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 ==0:
        s += c
        i += 1
print(f'A soma dos números ímpares divisiveis por 3 de 1 até 500, sendo eles {i} valores, é {s}')