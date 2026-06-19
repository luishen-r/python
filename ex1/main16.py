import random

vetor = [random.randint(1, 10) for _ in range(10)]

print("Vetor gerado:")
print(vetor)

contagem = {}

for num in vetor:
    contagem[num] = contagem.get(num, 0) + 1

repetidos = {num: qtd for num, qtd in contagem.items() if qtd > 1}

if repetidos:
    print("\nValores repetidos encontrados:")
    for num, qtd in repetidos.items():
        print(f"Valor {num} aparece {qtd} vezes")
else:
    print("\nNão existem valores repetidos no vetor.")