listas = [
    [1, 2, 2, 3, 4],
    [1, 1 , 2 , 4, 5],
    [1, 2, 3, 4, 4, 5, 6],
    [1, 3 , 4, 2, 5, 5]   
]


def encontrar_primeiro_repetido(lista):
    numero_duplicado = 0
    numeros_checados = set()
    
    for numero in lista:
        if numero in numeros_checados:
            numero_duplicado = numero
            break
        
        numeros_checados.add(numero)

    return numero_duplicado

for lista in listas:
    print(lista, encontrar_primeiro_repetido(lista))
    print()