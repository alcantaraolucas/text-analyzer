def contar_caracteres_com_espacos(texto):
    """Conta o número total de caracteres no texto, incluindo espaços."""
    return len(texto)

def contar_caracteres_sem_espacos(texto):
    """Conta o número total de caracteres no texto, excluindo espaços."""
    return len(texto.replace(" ", ""))
