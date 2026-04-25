def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
    finally:
        a.close()


def novoCadastro(nome, usuario='<Desconhecido>', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{usuario};{idade}\n')
        except:
            print('ERRO ao escrever os dados!')
        else:
            print(f'Novo usuário {usuario} adicionado com sucesso!')
        finally:
            a.close()