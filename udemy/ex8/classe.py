import json

CAMINHO_ARQUIVO = 'exercicio8.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 21)
p2 = Pessoa('Luis', 18)

bd = [vars(p1), vars(p2)]

def dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    dump()