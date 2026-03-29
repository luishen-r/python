import math
n = int(input('Digite o valor do ângulo:'))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print(f'O valor do seno é: {seno:.2f}')
print(f'O valor do cosseno é: {cos:.2f}')
print(f'O valor da tangente é: {tg:.2f}')
