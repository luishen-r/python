l1 = float(input('Valor do lado do triângulo: '))
l2 = float(input('Valor do lado do triângulo: '))
l3 = float(input('Valor do lado do triângulo: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Esse triângulo está conforme sua condição de existência')
else:
    print('Esse triângulo foge à condição de existência')
