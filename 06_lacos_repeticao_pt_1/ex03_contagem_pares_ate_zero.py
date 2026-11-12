"""
Construa um programa onde o usuário digitará um número e o programa
completará o número digitado até 0, apenas com números pares.
"""

# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Estrutura de decisão: define o sentido da contagem
if numero < 0:
    # Se o número for ímpar, soma 1 para obter o par mais próximo de 0
    if numero % 2 != 0:
        numero += 1

    # Laço de repetição: imprime enquanto o número for menor ou igual a 0,
    # somando 2 a cada iteração (apenas pares)
    while numero <= 0:
        print(numero)

        numero += 2
else:
    # Se o número for ímpar, subtrai 1 para obter o par mais próximo de 0
    if numero % 2 != 0:
        numero -= 1

    # Laço de repetição: imprime enquanto o número for maior ou igual a 0,
    # subtraindo 2 a cada iteração (apenas pares)
    while numero >= 0:
        print(numero)

        numero -= 2
