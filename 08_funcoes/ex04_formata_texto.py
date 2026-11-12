"""
Crie uma função que coloque qualquer texto no seguinte padrão e o retorne:
◆ Tudo em minúscula.
◆ Sem espaços na frente ou atrás (começando e finalizando o texto).
"""


def formata_texto(texto: str) -> str:
    """Retorna o texto em minúsculas e sem espaços nas extremidades."""
    return texto.strip().lower()


texto = input("Digite um texto: ")

print(f"\nTexto formatado: {formata_texto(texto)}")
