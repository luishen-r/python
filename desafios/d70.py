totcompra = 0
maisde1k = 0
barato = 0
cont = 0
prodmaisbarato = ' '
while True:
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    resp = ' '
    totcompra += preco
    if cont == 0:
        prodmaisbarato = nomep
        barato = preco
    else:
        if preco < barato:
            barato = preco
            prodmaisbarato = nomep
    if preco > 1000:
        maisde1k += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if resp == 'N':
        print(f'{"FIM DO PROGRAMA":=^40}')
        break
print(f'O total de compras foi de R${totcompra}')
print(f'Temos {maisde1k} custando mais de R$1000')
print(f'O produto mais barato foi {prodmaisbarato} que custou R${barato}')

