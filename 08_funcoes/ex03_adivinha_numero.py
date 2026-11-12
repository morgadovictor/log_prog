"""
O programa irá sortear um número entre 1 e 100, e temos que adivinhar qual
foi esse número.
"""

import random


def sortear_numero() -> int:
    """Retorna um inteiro aleatório entre 1 e 100."""
    return random.randint(1, 100)


adivinhacao = None
numero_sorteado = sortear_numero()
tentativas = 0

while adivinhacao != numero_sorteado:
    adivinhacao = int(input("\nTente adivinhar (1 a 100): "))
    tentativas += 1

    if adivinhacao > numero_sorteado:
        print("O número digitado é MAIOR do que o número sorteado.")
    elif adivinhacao < numero_sorteado:
        print("O número digitado é MENOR do que o número sorteado.")

print(f"\nParabéns! Você acertou em {tentativas} tentativa(s).")
print(f"O número era {numero_sorteado}!")
