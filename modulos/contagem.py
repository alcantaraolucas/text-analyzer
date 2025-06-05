def contar_palavras(texto):
    """Conta o número de palavras em um texto."""
    if not texto:
        return 0
    palavras = texto.split()
    return len(palavras)
