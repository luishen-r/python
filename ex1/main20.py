def ler_matriz():
    matriz = []
    
    for l in range(3):
        linha = []
        for c in range(3):
            valor = int(input(f'Informe o valor da posicão [{l+1}][{c+1}]'))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def analisar_matriz(matriz):
    soma_colunas = []
    for l in range(3):
        soma = 0
        for c in range(3):
            soma += matriz[c][l]
        soma_colunas.append(soma)
    
    soma_linhas = []
    for linha in matriz:
        soma_linhas.append(sum(linha))
    
    coluna_maior_valor = soma_colunas.index(max(soma_colunas)) 
    linha_menor_valor = soma_linhas.index(min(soma_linhas))
    
    print(f'\nColuna que possui o maior valor: {coluna_maior_valor+1}')
    print(f'Soma dos valores: {soma_colunas[coluna_maior_valor]}')
    
    print(f'\nLinha com menor valor: {linha_menor_valor+1}')
    print(f'Soma dos valores: {soma_linhas[linha_menor_valor]}')
    

matriz = ler_matriz()
analisar_matriz(matriz)