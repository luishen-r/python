preco = float(input('Qual o preço do produto? R$'))
desconto = preco*(5/100)
precodes = preco-desconto
print('O preço desse produto é {}, com o desconto de 5% aplicado, o preço final é de R${:.2f}'.format(preco, precodes))
