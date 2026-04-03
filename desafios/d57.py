sexo = 'M' or 'F'
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Valor inválido, tente novamente: ')).upper().strip()[0]
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Valor inválido, tente novamente: ')).upper().strip()[0]
        