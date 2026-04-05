conth = 0
p18 = 0
mulher20 = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRO DE PESSOA": ^15}')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        p18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas na maior idade foi {p18}')
print(f'O total de homens que acesseram o programa foi {conth}')
print(
    f'O total de mulheres com menos de 20 anos que acessaram o programa foi {mulher20}')
