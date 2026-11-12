"""
Construa um jogo de pedra, papel e tesoura.
"""

import random

opcoes = ["pedra", "papel", "tesoura"]

# Solicita a jogada do usuário, removendo espaços extras (.strip())
# e convertendo para minúsculas (.lower())
jogador = input("\nEscolha: pedra, papel ou tesoura? ").lower().strip()

if jogador not in opcoes:
    print("\nEscolha inválida! Tente novamente.")
else:
    # Seleciona aleatoriamente uma opção para o computador
    computador = random.choice(opcoes)

    # Exibe a escolha feita pelo usuário e pelo computador
    print(f"\nVocê escolheu {jogador}")
    print(f"O computador escolheu {computador}")

    # Verifica as condições de vitória, empate ou derrota
    # Caso 1: Escolhas iguais resultam em empate
    if jogador == computador:
        print("\nEmpate.")
    # Caso 2: Condições onde o jogador ganha
    # (Pedra > Tesoura, Papel > Pedra, Tesoura > Papel)
    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("\nVocê ganhou!")
    # Caso 3. Se não empatou e o jogador não venceu,
    # o computador venceu obrigatoriamente
    else:
        print("\nO computador ganhou.")
