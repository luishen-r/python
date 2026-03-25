n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print('A média entre {} e {} é igual a {}'.format(n1, n2, m))
if m >= 7:
    print('Parabéns, você foi aprovado!')
else:    print('Infelizmente, você foi reprovado. Estude mais para a próxima!')