def somador(n):
    if n == 0:
        return 0
    
    return n + somador(n-1)


num = int(input('Digite um valor: '))
print(f'Soma de 1 até {num} = {somador(num)}')
