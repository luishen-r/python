fr = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {fr.count("A")} vezes')
print(f'A primeira letra A aparece na posição {fr.find("A")+1}')
print(f'A última letra A aparece na posição {fr.rfind("A")+1-fr.count(" ")}')
