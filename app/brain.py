def interpretar(comando):

    comando = comando.lower()

    if "histórico" in comando or "historico" in comando:
        return "SHOW_HISTORY"  # Adicionado espaço após SHOW_HISTORY

    if "meu nome é" in comando:
        return "SET_NAME"  # Adicionado espaço após SET_NAME

    if "qual meu nome" in comando:
        return "GET_NAME"  # Adicionado espaço após GET_NAME

    if "youtube" in comando:
        return "OPEN_YOUTUBE"  # Adicionado espaço após OPEN_YOUTUBE

    if "hora" in comando:
        return "GET_TIME"  # Adicionado espaço após GET_TIME

    return "UNKNOWN"  # Adicionado espaço após UNKNOWN
