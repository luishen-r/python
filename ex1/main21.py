def soma_diagonal(matriz):
    soma = 0
    
    for i in range(3):
        soma += matriz[i][i]
    
    return soma


matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f'Informe o valor da posição [{l+1}][{c+1}]: '))
        linha.append(valor)
    matriz.append(linha)

print(f'Soma da diagonal principal: {soma_diagonal(matriz)}')