def interpretar(comando):
    comando = comando.lower()

    if "youtube" in comando:
        return "OPEN_YOUTUBE"

    if "hora" in comando:
        return "GET_TIME"

    return "UNKNOWN"