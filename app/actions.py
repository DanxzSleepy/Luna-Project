from datetime import datetime
from memory import carregar_memoria, salvar_memoria


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


    print("Luna: Não entendi.")