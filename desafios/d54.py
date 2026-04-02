from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c} pessoa nasceu? '))
    idade = atual - nasc
    if idade >=18:
        maior += 1
    else:
        menor += 1
print(f'O número de pessoa maiores de idade é {maior}, e o número de pessoas menores de idade é {menor}')
    