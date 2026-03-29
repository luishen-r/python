sal = float(input('Digite o valor do seu salário: '))
if sal <= 1250:
    newsal = sal+(sal*15/100)
else:
    newsal = sal+(sal*10/100)
print(f'O salário de R${sal:.2f}, passa a ser R${newsal:.2f}')
