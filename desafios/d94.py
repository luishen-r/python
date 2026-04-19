pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Digite novamente')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Digite novamente')
        else:
            break
    if resp == 'N':
        break

media = soma/len(galera)
print('-='*30)
print(f'Ao todo temos cadastrados {len(galera)} pessoas')
print(f'A média de idade das pessoas cadastradas é {media:.2f}')
print(f'As mulheres cadastradas foram ', end='')

for  p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end=' ')

print()
print('As pessoas que estão acima da média são: ')

for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} com {p["idade"]} anos')
        