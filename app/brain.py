def interpretar(comando):

    comando = comando.lower()

    if "meu nome é" in comando:
        return "SET_NAME"

    if "qual meu nome" in comando:
        return "GET_NAME"

    if "youtube" in comando:
        return "OPEN_YOUTUBE"

    if "hora" in comando:
        return "GET_TIME"

    return "UNKNOWN"