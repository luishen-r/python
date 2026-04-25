def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    print('-' * tam)


def menu():
    linha()
    print(f'{"MENU PRINCIPAL".center(42)}')
    linha()


def submenu(lista):
    for i, item in enumerate(lista):
        print(f'{i + 1} - {item}')
    print('0 - Voltar')
    linha()
    opc = leiaInt('Sua opção: ')
    return opc
    