from utilidades import moedas
from utilidades import dados
p = dados.leiaDinheiro('Digite o preço: R$ ')
t = dados.leiaTaxa('Digite a taxa desejada: ')
moedas.resumo(p, t)