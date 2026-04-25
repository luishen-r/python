import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moedas.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moedas.dobro(p):.2f}')

taxa = float(input('Digite a taxa de aumento: '))
print(f'Com um aumento de {taxa}%, o preço fica em R$ {moedas.aumentar(p, taxa):.2f}')
print(f'Com uma redução de {taxa}%, o preço fica em R$ {moedas.diminuir(p, taxa):.2f}')