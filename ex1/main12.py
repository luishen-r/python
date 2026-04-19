pessoas = dict()
pessoas['nome'] = 'Luis'
pessoas['idade'] = 18
pessoas['sexo'] = 'M'
pessoas['peso'] = 71.6
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
estado1 = {'UF': 'Ceará', 'Capital': 'Fortaleza', 'População(em milhões)': 2.57}
estado2 = {'UF': 'Piauí', 'Capital': 'Teresina', 'População(em milhões)': 3.28}
nordeste = list()
nordeste.extend([estado1, estado2])
for e in nordeste:
    for k, v in e.items():
        print(f'{k} = {v}')
    print()