"""
Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
dos valores digitados deverão ser calculadas.
"""

matriz = []

for i in range(2):
    linha = []

    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]:"))
        linha.append(valor)

    matriz.append(linha)

soma = sum(sum(linha) for linha in matriz)
media = soma / (len(matriz) * len(matriz[0]))

print(f"\nSoma dos valores digitados: {soma}")
print(f"Média dos valores digitados: {media:.2f}")
