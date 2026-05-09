pessoa = {
    "nome" : "Luis",
    "idade" : 18,
    "altura" : 1.87,
    "peso" : 72 
}

(a1, a2), b, c, d = pessoa.items()
print(a1, a2, b, c, d)

#def mostrar_dict(**kwargs):
    #for k, v in kwargs.items():
       #print(f'{k}: {v}')


#mostrar_dict(**pessoa)