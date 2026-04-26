#Treinando dict
while True:
    estoque = {"maçã": 10, "banana": 5, "laranja": 8}
    busca = ''
    search = input("Digite o nome da fruta que deseja buscar: ")
    if search.lower() == 'sair':
        print("Encerrando o programa.")
        break
    busca = search.lower()
    if busca not in estoque:
        print(f"{busca} não encontrada no estoque.")
        print("Adicionando ao estoque com quantidade 0.")
    estoque.setdefault(busca, 0)
    print(f"Quantidade de {busca}: {estoque[busca]}")


produtos = {'Laptop': 1500, 'Smartphone': 800, 'Tablet': 600, 'Monitor': 700, 'Teclado': 100} 
print('--------Tabela de Produtos--------')    
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
    preco_desconto = preco * 0.9
    print(f"Preço com desconto de 10%: R$ {preco_desconto:.2f}")


print('\n ---Busca de Produto---')
while True:
    busca_produto = input("Digite o nome do produto para buscar (ou 'sair' para encerrar): ")
    resultado = produtos.get(busca_produto, 'Produto não cadastrado')
    if busca_produto.lower() == 'sair':
        print("Encerrando a busca.")
        break
    print(f'Resultado da busca {busca_produto}: {resultado}')    


def contar_palavra(texto):
    texto = texto.lower()
    pontuação = [',', '.', '!', '?', ';', ':', '-', '(', ')', '"', "'"]
    for p in pontuação:
        texto = texto.replace(p, '')
    palavra = texto.split()
    contagem = {}
    for p in palavra:
        contagem[p] = contagem.get(p, 0) + 1     
    return contagem


frase = str(input("Digite uma frase para contar as palavras: "))
resultado_contagem = contar_palavra(frase)
print("Contagem de palavras:")
for palavra, contagem in resultado_contagem.items():
    print(f"{palavra}: {contagem}")  