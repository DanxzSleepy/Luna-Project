from datetime import datetime
from memory import carregar_memoria, salvar_memoria, carregar_historico, salvar_historico


def executar(acao, comando):

    memoria = carregar_memoria()

    if acao == "SET_NAME":

        nome = comando.replace("meu nome é", "").strip()

        memoria["nome"] = nome

        salvar_memoria(memoria)

        print("Luna: Entendido.")
        return


    if acao == "GET_NAME":

        nome = memoria["nome"]

        if nome:
            print(f"Luna: Seu nome é {nome}.")
        else:
            print("Luna: Ainda não sei seu nome.")

        return


    if acao == "GET_TIME":
        print("Luna:", datetime.now().strftime("%H:%M"))
        return


    if acao == "OPEN_YOUTUBE":
        print("Luna: Abrindo YouTube...")
        return
    
    if acao == "SHOW_HISTORY":

        historico = carregar_historico()

    if not historico:
        print("Luna: Nenhum comando registrado.")
        return

    print("Luna: Histórico:")

    for i, item in enumerate(historico[-10:], start=1):
        print(f"{i}. {item}")

    return

    print("Luna: Não entendi.")