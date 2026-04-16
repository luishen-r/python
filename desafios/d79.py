num = list()
while True:
    n = int(input("Digite um número: "))
    if n in num:
        print(f"O número {n} já foi digitado, tente outro.")
    else:
        num.append(n)
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    if r == "N":
        break
print(f"Você digitou os valores {sorted(num)}")