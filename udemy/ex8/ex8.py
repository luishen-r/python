import json
from classe import Pessoa, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

dados = [Pessoa(**pessoa) for pessoa in dados]

for p in dados:
    print(p.nome, p.idade)