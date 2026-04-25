def resumo(preco=0, taxa=0):
    def aumentar(preco=0, taxa=0, formato=False):
        res = preco + (preco * taxa / 100)
        if formato:
            return moeda(res)
        return res

    def diminuir(preco=0, taxa=0, formato=False):
        res = preco - (preco * taxa / 100)
        if formato:
            return moeda(res)
        return res      

    def dobro(preco=0, formato=False):
        res = preco * 2
        if formato:
            return moeda(res)
        return res


    def metade(preco=0, formato=False):
        res = preco / 2
        if formato:
            return moeda(res)
        return res


    def moeda(preco=0, moeda='R$'):
        return f'{moeda}{preco:.2f}'.replace('.', ',')
    
    
    print('-'*30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-'*30)
    print()
    print(f'Preço analisado: {moeda(preco).rjust(15)}')
    print(f'Dobro do preço: {dobro(preco, True).rjust(15)}')
    print(f'{taxa}% de aumento: {aumentar(preco, taxa, True).rjust(15)}')
    print(f'{taxa}% de diminuição: {diminuir(preco, taxa, True).rjust(13)}')