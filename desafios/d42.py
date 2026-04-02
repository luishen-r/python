print(f'{"LOJAS AMERICANAS":=^40}')
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opt = int(input('Qual opção: '))
if opt == 1:
    npreco = preco - (preco*0.1)
    print(f'O valor a ser pago será de {npreco} reais')
elif opt == 2:
    npreco = preco - (preco*0.05)
    print(f'O valor a ser pago será de {npreco} reais')
elif opt == 3:
    print(f'O valor a ser pago será de {preco} reais')
elif opt == 4:
    npreco = preco + (preco*0.2)
    parcela = int(input('Em quantas parcelas? '))
    precoparc = npreco / parcela
    print(f'O valor a ser pago será de {npreco} reais')
    print(f'Com parcelas em valor de {precoparc} reais')
else:
    print('OPÇÃO INVÁLIDA!')
