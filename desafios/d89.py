ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(ficha):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[2]:>8.2f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}')