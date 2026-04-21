def maior(*num):
    if len(num) == 0:
        print('-='*30)
        print('Nenhum valor foi informado.')
        print('-='*30)
        return
    elif num == (0,):
        print('-='*30)
        print('O valor é nulo.')
        print('-='*30)
        return
    print('-='*30)
    print('Analisando os valores passados...')
    print(f'Foram informados {len(num)} valores ao todo.')
    print('Os valores são: ', end='')
    for n in num:
        print(f'{n} ', end='')
    print()  # Imprime uma nova linha após os valores
    maior = max(num)  # Encontra o maior valor usando a função max()
    print(f'O maior valor informado foi {maior}.')
    print('-='*30)


maior(2, 9, 4, 5, 7, 1)
maior(0)