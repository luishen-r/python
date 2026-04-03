from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float (input('Segundo valor: '))
choose = 0
while choose != 5:
    choose= int(input('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        Qual a sua opção? '''))
    if choose == 1:
        res = n1 + n2
        print(f'A soma entre {n1} e {n2} é {res}')
    elif choose == 2:
        res = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {res}')
    elif choose == 3:
        if n1 > n2:
            print(f'O valor {n1} é o maior')
        elif n1 == n2:
            print('Os valores são iguais')
        else:
            print(f'O valor {n2} é maior')
    elif choose == 4:
        print('Digite os números novamente!')
        n1 = float(input('Primeiro valor: '))
        n2 = float (input('Segundo valor: '))
    elif choose == 5:
        print('Saindo do programa...')
        sleep(2)
        print('Programa finalizado')
    else:
        print('Opção inválida, tente novamente')
       