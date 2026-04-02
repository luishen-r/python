print(f'{"DETECTOR DE PALÍNDROMOS":=^40}')
fr = str(input('Digite uma frase: ')).strip().upper()
word = fr.split()
junto = ''.join(word)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
