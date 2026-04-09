cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente.', end='')
while True:
    print(f'Você digitou o número {cont[num]}')
    pergunta = str(input('Você quer continuar?[S/N] '))
    resp = pergunta.strip().upper()
    if resp not in 'SN':
       pergunta = str(input('Você quer continuar?[S/N] '))
    if resp == 'N':
        print('FIM')
        break
    else:
        print('Vamos denovo!')
    while True:
        num = int(input('Digite um número entre 0 e 10: '))
        if 0 <= num <= 10:
            break
        print('Tente novamente.', end='')