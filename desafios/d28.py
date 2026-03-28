import random
from time import sleep
print('Vou pensar em um número de 0 a 5')
print('PENSANDO...')
sleep(3)
n=int(input('Tente adivinhar que número eu pensei: '))
r=random.randint(0,5)
print(f'Eu pensei em {r}')
if n == r:
    print('Parabéns você acertou!')
else:
    print('Não foi dessa vez, tente denovo!')
