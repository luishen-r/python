from functools import wraps

usuario_atual = {"logado": False, "Usuário": "Visitante"}


def exige_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if usuario_atual["logado"] == True:
            return func(*args, **kwargs)
        else:
            print("Acesso Negado. Login é necessário para o devido acesso.")
    return wrapper
        

@exige_login
def saldo_banco(valor):
    print(f"Saldo: R${valor}")


usuario_atual["logado"] = True
saldo_banco(400)

    