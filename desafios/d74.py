import random
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort = random.shuffle(numeros)
print(f'Eu sorteei os valores {numeros[0:5]}')
print(f'O maior valor foi {max(numeros[0:5])}')
print(f'O menor valor foi {min(numeros[0:5])}')
