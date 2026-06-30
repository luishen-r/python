def permutar(str, prefixo=''):
    if len(str) == 0:
        print(prefixo)
        return
    
    for i in range(len(str)):
        char = str[i]
        resto = str[:i] + str[i+1:]
        permutar(resto, prefixo + char)
        

msg = (input('Digite uma string: '))
print(permutar(msg))