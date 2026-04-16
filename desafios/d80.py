lista = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if not lista or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
        print(f'O valor foi adicionado na posição {pos} da lista')
print(f'Os valores inseridos, em ordem, foram {lista}')