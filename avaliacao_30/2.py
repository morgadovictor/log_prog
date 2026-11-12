"""
Desenvolva um programa em Python que leia 10 números inteiros
e os armazene em um vetor original.
A partir dessa estrutura, crie duas novas listas independentes:
uma lista denominada pares, contendo cada número par do vetor original
multiplicado por 3, e uma lista denominada ímpares, contendo os números ímpares
mantidos com seus valores inalterados.
Ao final, o programa deve exibir o vetor original, os dois novos vetores
resultantes e a contagem exata de elementos alocados em cada um deles.
"""

# Cria uma lista vazia chamada {numeros}
numeros = []
numeros_pares_x3 = []
numeros_impares = []
contador = 0

# Loop que solicita 10 números inteiros ao usuário
for i in range(10):
    # Validação do número ser inteiro
    while True:
        try:
            numero = int(input(f"\nDigite o {i + 1}º número: "))
            break
        except ValueError:
            print("\nErro: Digite um número inteiro.")

    # Integra o número digitado na lista {numeros}
    numeros.append(numero)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares_x3.append(numeros[i] * 3)
    else:
        numeros_impares.append(numeros[i])

print("\n", end="=" * 60)
print("\nExibição da Lista Original:\n")

# Loop para exibir {numeros}
for i in range(len(numeros)):
    contador += 1

    if i != len(numeros) - 1:
        print(numeros[i], end=" - ")
    else:
        print(numeros[i])

print(f"\nContagem Exata de Elementos Alocados: {contador}")
print("=" * 60)

# Zera o contador
contador = 0

print("\n", end="=" * 60)
print("\nExibição da Lista Somente Pares x3:\n")

# Loop para exibir {numeros_pares_x3}
for i in range(len(numeros_pares_x3)):
    contador += 1

    if i != len(numeros_pares_x3) - 1:
        print(numeros_pares_x3[i], end=" - ")
    else:
        print(numeros_pares_x3[i])

print(f"\nContagem Exata de Elementos Alocados: {contador}")
print("=" * 60)

# Zera o contador novamente
contador = 0

print("\n", end="=" * 60)
print("\nExibição da Lista Somente Ímpares:\n")

# Loop para exibir {numeros_impares}
for i in range(len(numeros_impares)):
    contador += 1

    if i != len(numeros_impares) - 1:
        print(numeros_impares[i], end=" - ")
    else:
        print(numeros_impares[i])

print(f"\nContagem Exata de Elementos Alocados: {contador}")
print("=" * 60)
