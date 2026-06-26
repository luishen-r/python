def calcular_saque(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    
    if valor < 4:
        return 'Valor inválido. Saque mínimo de R$4.'
    
    resto = valor
    resultado = {}
    
    for cedula in cedulas:
        quantidade = resto // cedula
        
        if quantidade > 0:
            resultado[cedula] = quantidade
            resto %= cedula
        
    if resto != 0:
        return 'Não é possível realizar esse saque com as cédulas disponíveis.'
    
    for cedula, quantidade in resultado.items():
        print(f'{quantidade} cédula(s) de R${cedula}')
    

valor = int(input('Informe o valor de saque: '))
calcular_saque(valor)