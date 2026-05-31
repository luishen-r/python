def zipper(*args):
    tam =  min(len(arg) for arg in args)
    return  [tuple(arg[i] for arg in args) for i in range(tam) 
    ]
    
    
list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
zipper_list = zipper(list1, list2)
print(zipper_list)    