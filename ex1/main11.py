nomes = ('Luis', 'Larissa', 'Ramon', 'Filho')
# Tuplas são imutáveis
for pos, c in enumerate(range(0, len(nomes))):
    print(nomes[c], pos)
print(sorted(nomes))
pessoa = ('Luis', 18, 'M')
print(pessoa[0:])
filme = ('O Poderoso Chefão', 1972, 'Francis Ford Coppola')
titulo = filme[0]
ano = filme[1]
diretor = filme[2]
print(f'O filme {titulo} foi lançado em {ano} e dirigido por {diretor}')