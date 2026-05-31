import json

def carregar_memoria():
    with open("data/memory.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)