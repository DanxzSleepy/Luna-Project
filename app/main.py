# app/main.py

print("Luna iniciada")

from brain import interpretar
from actions import executar
from memory import carregar_historico, salvar_historico


while True:

    comando = input("Você: ")
    historico = carregar_historico()
    historico.append(comando)
    salvar_historico(historico)

    if comando == "sair":
        break

    acao = interpretar(comando)
    executar(acao, comando)
