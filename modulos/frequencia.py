import re

def obter_frequencia_palavras(texto):
    """Retorna um dicionário com a frequência de cada palavra."""
    if not texto:
        return {}
    palavras = re.findall(r'\b\w+\b', texto.lower()) # Pega palavras, ignora pontuação, converte para minúsculas
    freq = {}
    for palavra in palavras:
        freq[palavra] = freq.get(palavra, 0) + 1
    return freq
