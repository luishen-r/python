n = int(input('Digite um número: '))
print('''Escolha o qual opção você deseja transformar esse número
      [1]Binário
      [2]Hexadecimal
      [3]Octal''')
choose = int(input('Qual opção você quer? '))
if choose == 1:
    print(f'{bin(n[2:])}')
elif choose == 2:
    print(f'{hex(n[2:])}')
elif choose == 3:
    print(f'{oct(n[2:])}')
