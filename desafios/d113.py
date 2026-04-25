def leiaInt(msg):
    """Verificador de número inteiro

    Args:

    Returns:
        int: O número inteiro digitado pelo usuário.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    """Verificador de número real

    Args:
        msg (str): A mensagem a ser exibida para o usuário solicitar a entrada de um número real.

    Returns:
        float: O número real digitado pelo usuário.
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {f}.')