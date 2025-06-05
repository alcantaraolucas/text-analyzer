def contar_linhas(texto):
    """Conta o número de linhas no texto."""
    if not texto:
        return 0
    return len(texto.split('\n'))

def contar_sentencas(texto):
    """Conta o número de sentenças (baseado em '.', '!', '?')."""
    if not texto:
        return 0
    count = 0
    for char in texto:
        if char in ['.', '!', '?']:
            count += 1
    return count if count > 0 else (1 if texto else 0) # Considera uma sentença se houver texto sem pontuação final
