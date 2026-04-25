try:
    numero = int(input("Insira um número: "))
    resultado = 100 / numero
except ValueError, TypeError:
    print("Por favor, insira um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("O resultado da divisão é:", resultado)