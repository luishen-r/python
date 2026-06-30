def inverte(str):
    if len(str) <= 1:
        return str
    
    return str[-1] + inverte(str[:-1])


palavra = str(input('Digite uma palavra: '))
print(f'Inversão: {inverte(palavra)}')