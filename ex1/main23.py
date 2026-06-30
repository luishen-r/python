from random import randint

def maior_valor(vetor, indice=0):
    if indice == len(vetor) - 1:
        return vetor[indice]

    maior_restante = maior_valor(vetor, indice + 1)

    if vetor[indice] > maior_restante:
        return vetor[indice]
    else:
        return maior_restante


vetor = [randint(1, 100) for _ in range(10)]

print(f'Vetor gerado: {vetor}')
print(f'Maior valor: {maior_valor(vetor)}')