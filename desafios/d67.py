while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'-- Tabuada de {n} --')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
print('Programa de tabuada encerrado. Volte sempre!')