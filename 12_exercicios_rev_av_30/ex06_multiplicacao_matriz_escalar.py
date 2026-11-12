"""
Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
números inteiros e, em seguida, peça ao usuário um valor numérico constante
(escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar
cada elemento da matriz original por esse valor escalar e exibir a matriz
resultante formatada em linhas e colunas.
"""

matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        linha.append(int(input(f"Digite o número de [{i}] [{j}]: ").strip()))

    matriz.append(linha)

print(matriz)

constante = int(input("\nAgora digite a constante: ").strip())

print()

for i in range(3):
    for j in range(3):
        matriz[i][j] *= constante

        print(matriz[i][j], end="\t")

    print()
