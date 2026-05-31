import json

ARQUIVO = "data/memory.json"


def carregar_memoria():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_memoria(memoria):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)