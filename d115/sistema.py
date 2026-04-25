from biblioteca import interfacesist
from biblioteca.arquivo import arquivoExiste, criarArquivo, lerArquivo, novoCadastro
from time import sleep

arquivo = 'usuarios.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
while True:
    interfacesist.menu()
    opc = interfacesist.submenu(['Cadastrar Usuários', 'Mostrar Usuários'])
    if opc == 1:
        print('Opção de cadastrar usuários selecionada.')
        nome = str(input('Digite o nome do usuário: ')).strip()
        idade = interfacesist.leiaInt('Digite a idade do usuário: ')
        novoCadastro(arquivo, nome, idade)
    elif opc == 2:
        print('Opção de mostrar usuários selecionada.')
        lerArquivo(arquivo)
    elif opc == 0:
        print('Saindo do programa...')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)