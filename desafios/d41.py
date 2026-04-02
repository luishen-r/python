l1 = float(input('Digite o valor do segmento: '))
l2 = float(input('Digite o valor do segmento: '))
l3 = float(input('Digite o valor do segmento: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Esses valores podem formar um triângulo!')
    if l1 == l2 and l2 == l3:
        print('Esse triângulo é equilátero')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Esse triângulo é escaleno!')
    else:
        print('Esse triângulo é isosceles!')
else:
    print('Não é possível formar um triângulo!')