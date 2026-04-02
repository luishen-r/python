peso = float(input('Qual o seu peso? '))
alt = float(input('Qual sua altura em metros ?'))
imc = (peso / (alt**2))
if imc <= 18.5:
    print(f'Seu imc é {imc:.2f}')
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.2f}')
    print('Peso ideal')
elif 25<= imc <= 30:
    print(f'Seu imc é {imc:.2f}')
    print('Sobrepeso')
elif 30<= imc <=40:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade')
else:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade mórbida')