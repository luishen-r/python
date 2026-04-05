from random import randint
while True:
    print('-=' * 20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 20)
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    computador = ' '
    while escolha not in 'PI':
        escolha = str(input('[P/I]? ')).strip().upper()[0]
    computn = randint(0, 10)
    s = jogador + computn
    print(f'O computador escolheu {computn}')
    print(f'A soma dessas dois é {s}')
    if jogador + computn % 2 == 0:
        print('PAR!')
        if escolha == 'P':
            print('Você venceu')
            print('Vamos denovo!')
        else:
            print('Você perdeu :C')
            break
    elif jogador + computn % 2 != 0:
        print('ÍMPAR')
        if escolha == 'I':
            print('Você venceu')
            print('Vamos denovo!')
        else:
            print('Você perdeu :C')
            break