"""
Um formulário web despadronizado gerou um arquivo de texto bruto
chamado emails_brutos.txt com e-mails digitados pelos usuários.
i. Esse arquivo contém espaçamentos indesejados nas pontas, caracteres
maiúsculos misturados e linhas vazias acidentais.
ii. Escreva um script em Python que leia esse arquivo linha por linha,
descarte linhas em branco, converta todos os e-mails válidos
para letras minúsculas (lowercase), remova espaços extras nas pontas
e salve a lista limpa e padronizada em um novo arquivo chamado
emails_padronizados.txt.
"""

from pathlib import Path

pasta = Path(__file__).parent  # pasta onde este .py está
entrada_path = pasta / "emails_brutos.txt"
saida_path = pasta / "emails_padronizados.txt"

with open(entrada_path, "r", encoding="utf-8") as entrada, open(
    saida_path, "w", encoding="utf-8"
) as saida:
    for email in entrada:
        if email.strip() != "":
            saida.write(f"{email.strip().lower()}\n")
