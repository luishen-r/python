somaidade = 0
homemvelho = ''
idadehomem = 0
mulher20 = 0
for p in range(1, 5):
    print(f'{p} {"PESSOA":-^20}')
    nome = str(input('Digite o seu nome:'))
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe o seu sexo [F/M]: ')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        idadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(f'A média de idade do grupo é {somaidade/4} anos')
print(f'O homem mais velho tem {idadehomem} anos e se chama {homemvelho}')
print(f'O total de mulheres com menos de 20 anos é de {mulher20}')
    
