import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')

taxa = float(input('Digite a taxa de aumento: '))
print(f'Com um aumento de {taxa}%, o preço fica em {moedas.aumentar(p, taxa, True)}')
print(f'Com uma redução de {taxa}%, o preço fica em {moedas.diminuir(p, taxa, True)}')