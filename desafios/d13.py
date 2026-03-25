sal=float(input('Qual o salário do funcionário? R$'))
reajuste=sal*(15/100)
newsal=sal+reajuste
print('O seu salário de R${:.2f}, irá receber um reajuste de 15%, sendo {:.2f} em reais, o seu novo salário será de R${:.2f}'.format(sal, reajuste, newsal))          