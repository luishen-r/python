palavras = ('aprender', 'estudar', 'pensar', 'programar', 'esforço', 'linguagem',
            'lógica', 'python')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')
