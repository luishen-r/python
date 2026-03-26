import math
catop=float(input('Digite o valor do cateto oposto: '))
catadj=float(input('Digite o valor do cateto adjacente: '))
hip=math.hypot(catop,catadj)
print(f'O valor da hipotenusa desse triãngulo retângulo é: {hip:.2f}')