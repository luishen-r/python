exp = str(input('Digite a expressão: '))
lista = []
for s in exp:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Essa expressão não é válida')
