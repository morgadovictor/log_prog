"""
Atualize (ou crie uma nova) a função anterior para retornar se há um número
dentro do texto.
"""


def formata_texto(texto: str) -> str:
    """Retorna o texto em minúsculas e sem espaços nas extremidades."""
    return texto.strip().lower()


def tem_numero(texto: str) -> bool:
    """Retorna True se o texto contiver pelo menos um dígito."""
    return any(n.isdigit() for n in texto)


texto = input("Digite um texto: ")
formatado = formata_texto(texto)

print(f"\nTexto formatado: {formatado}")
print("Contém número." if tem_numero(formatado) else "Não contém número.")
