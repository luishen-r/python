def leiaDinheiro(p):
    while True:
        entrada = input(p).replace(',', '.').strip()
        # Verificamos se, após remover o ponto, o que sobra são apenas dígitos
        if entrada == '' or not entrada.replace('.', '', 1).isdigit():
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            return float(entrada)

def leiaTaxa(t):
    while True:
        entry = input(t).replace(',', '.').strip()
        # Se você quer aceitar apenas inteiros na taxa, usamos o .isdigit()
        if entry.isdigit():
            return int(entry)
        else:
            # Caso queira aceitar taxas decimais (ex: 5.5%), use a lógica do leiaDinheiro
            print(f'\033[0;31mERRO: "{entry}" não é uma taxa válida!\033[m')