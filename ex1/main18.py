from datetime import datetime

def dias_passados(data):
    dia, mes, ano = map(int, data.split('/'))
    
    if not (1 <= dia <= 30 and 1 <= mes <= 12 and ano > 0):
        return 'Data inválida.'
    
    hoje = datetime.now()
    
    total_data = ano * 365 + (mes - 1) * 30 + dia
    total_hoje = hoje.year * 365 + (hoje.month - 1) * 30 + hoje.day
    
    return total_hoje - total_data


data = input('Digite uma data (dd/mm/aaaa): ')
print(f'Já se passaram {dias_passados(data)} dias.')