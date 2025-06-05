from modulos.contagem import contar_palavras
from modulos.caracteres import contar_caracteres_com_espacos

def main():
    """Função principal do programa."""
    texto_exemplo = """Este é um texto de exemplo para nosso projeto de Git e GitHub.
Sejam bem-vindos!
Este projeto demonstra a colaboração e resolução de conflitos.
Boa sorte a todos os contribuidores."""

    print("Analisador de Texto Simples")
    print("---------------------------")
    print(f"Texto de entrada:\n\"{texto_exemplo}\"\n")

    # Análise inicial já implementada
    numero_de_palavras = contar_palavras(texto_exemplo)
    print(f"Número de palavras: {numero_de_palavras}")

    caracComEspaco= contar_caracteres_com_espacos(texto_exemplo)
    print(f'Caracteres com espaço: {caracComEspaco}')
    # Os alunos adicionarão as chamadas para as novas funcionalidades aqui.
    # Exemplo:
    # resultado_aluno_X = funcao_do_aluno_X(texto_exemplo)
    # print(f"Resultado Aluno X: {resultado_aluno_X}")

if __name__ == "__main__":
    main()
