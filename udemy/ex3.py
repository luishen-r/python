perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for p in perguntas:
    print(f"Pergunta: {p['Pergunta']}")
    print("Opções: ")
    
    opcoes = p['Opções']
    for i, o in enumerate(p['Opções']):
        print(f'{i+1}) {o}')
    resposta_usuario = input("Digite a resposta correta: ")
    
    try:
        if resposta_usuario.isdigit():
            resposta_usuario = int(resposta_usuario)
    except (ValueError, IndexError):
        print("Resposta inválida.")
        continue
    else:
        if resposta_usuario > 0 and resposta_usuario <= len(p['Opções']):
            if opcoes[resposta_usuario - 1] == p['Resposta']:
                print("Resposta correta!")
            else:
                print("Resposta incorreta.")
        else:
            print("Resposta inválida.")
    