# app/main.py

print("Luna iniciada")

from brain import interpretar
from actions import executar

while True:

    comando = input("Você: ")

    if comando == "sair":
        break

    acao = interpretar(comando)
    executar(acao, comando)
