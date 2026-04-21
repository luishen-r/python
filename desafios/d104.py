def leiaInt(msg):
    """Verificador de número inteiro

    Args:
        msg (str): A mensagem a ser exibida para o usuário solicitar a entrada de um número inteiro.

    Returns:
        int: O número inteiro digitado pelo usuário.
    """
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print('ERRO! Digite um número inteiro válido.')

n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')