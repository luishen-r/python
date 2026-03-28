from datetime import date as anoatual
year=int(input('Qual ano você deseja analisar? Coloque 0 para analisar o ano atual '))
if year==0:
    year=anoatual.today().year
if year%4==0 and year%100!=0 or year%400==0:
    print('Esse ano é BISSEXTO')
else:
    print('Esse ano não é BISSEXTO')