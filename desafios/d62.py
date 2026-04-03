print(f'{"Gerador de P.A":=^40}')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = a1
cont = 1
while cont <= 10:
    print(f'{t} ->', end='')
    t += r
    cont += 1
print('PAUSA')
mais = int(input('Quantos termos você quer mostrar a mais? '))
while mais != 0:
    cont = 1
    while cont <= mais:
        print(f'{t} ->', end='')
        t += r
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
