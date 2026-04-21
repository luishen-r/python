def fatorial(n, show=False):
    """Calcula o fatorial de um número.

    Args:
      para n(int): O valor o qual se deseja calcular o fatorial.
      para show(bool): Se True, mostra o processo de cálculo do fatorial, caso contrário, apenas retorna o resultado.

    Returns:
        int: O fatorial do número n.
    """
    if n < 0:
        return 'Não existe fatorial de número negativo.'
    if n == 0 or n == 1:
        return 1
    fat = 1
    print(f'{n}! = ', end='')
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        fat *= c
    return fat
    

num = int(input('Digite um número para calcular seu fatorial: '))
print(fatorial(num, show=True))