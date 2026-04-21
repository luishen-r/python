from time import sleep


def contador(inicio, passo, fim):
    if passo < 0:
        passo = abs(passo)
    elif passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            cont += passo
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            cont = cont - passo
            sleep(0.5)


print('='*30)
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 1, 10)
print()
print('='*30)

print('Contagem de 10 até 0 de 2 em 2:')
contador(10, 2, 0)
print()
print('='*30)

print('Contagem personalizada:')
inicio = int(input('Início: '))
passo = int(input('Passo: '))
fim = int(input('Fim: '))
contador(inicio, passo, fim)
print()