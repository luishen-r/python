import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p:.2f} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {p:.2f} é R$ {moedas.moeda(moedas.dobro(p))}')

taxa = float(input('Digite a taxa de aumento: '))
print(f'Com um aumento de {taxa}%, o preço fica em {moedas.moeda(moedas.aumentar(p, taxa))}')
print(f'Com uma redução de {taxa}%, o preço fica em {moedas.moeda(moedas.diminuir(p, taxa))}')