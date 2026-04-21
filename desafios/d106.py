def ajuda(com):
    help(com)


def titulo(msg):
    print('\033[1;30;44m~' * len(msg))
    print(msg)
    print('~' * len(msg) + '\033[m')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
