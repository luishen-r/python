lista = []
lista_menor = []
lista_maior = []
for c in range(0, 5):
    num = int(input(f"Digite um número na posição {c}: "))
    lista.append(num)
print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi {max(lista)}')
print(f'O menor número digitado foi {min(lista)}')
for p, v in enumerate(lista):
    if v == max(lista):
        lista_maior.append(p)
    if v == min(lista):
        lista_menor.append(p)
print(f'O maior número apareceu nas posições: {lista_maior}')
print(f'O menor número apareceu nas posições: {lista_menor}')