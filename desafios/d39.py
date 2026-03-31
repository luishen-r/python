from datetime import date as atual
nasc = int(input('Em que ano você nasceu? '))
ano = atual.today().year
idade = ano - nasc
print(f'Você possui {idade} anos')
if idade == 18:
    print('Você está na idade para realizar o alistamento militar!')
elif idade < 18:
    print('Você ainda não possui idade necessária para o alistamento militar')
    falta = 18 - idade
    print(f'Faltam {falta} anos até o seu alistamento!')
    print(f'Seu alistamento ocorrerá no ano de {ano + falta}')
else:
    print('Você ja passou da idade para o alistamento')
    datal = idade - 18
    print(f'Seu alistamento foi a {datal} anos atrás')
