def potencia(n):
    if n == 0:
        return 1
    
    return 2 * potencia(n-1)


valor = int(input('Informe um valor para ser o expoente: '))
print(f'Potenciação: {potencia(valor)}')