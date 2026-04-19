from datetime import date

trabalhador = dict()

trabalhador['nome'] = input('Nome: ')
trabalhador['idade'] = int(input('Idade: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - date.today().year)

for k, v in trabalhador.items():
    print(f'{k} = {v}')
