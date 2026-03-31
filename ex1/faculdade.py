freq = float(input('Informe sua frequência entre 0 e 1: '))
if freq >= 0.75:
    media = float(input('Informe quanto foi sua média: '))
    if media >= 7:
        print('Você foi aprovado, PARABÉNS!')
    elif media >= 3:
        print('Você irá para prova final')
    else:
        print('Você foi reprovado, estude mais da próxima vez!')
else:
    print('Você foi reprovado por faltas!')
