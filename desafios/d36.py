casa = float(input('Qual valor da casa? '))
sal = float(input('Qual o seu salário? '))
ano = int(input('Quantos anos de financiamento? '))
prestação = casa/(ano*12)
print(f'A prestação a ser paga será de {prestação:.2f}')
if prestação > sal*0.3:
    print('O financiamento não pode ser realizado pelo preço da prestação supera 30% do salário')
else:
    print('O financiamento pode ser concluido')
