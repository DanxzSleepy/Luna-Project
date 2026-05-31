from datetime import datetime

def executar(acao):

    if acao == "GET_TIME":
        print("Luna:", datetime.now().strftime("%H:%M"))
        return

    if acao == "OPEN_YOUTUBE":
        print("Luna: Abrindo YouTube...")
        return

    print("Luna: Não entendi.")