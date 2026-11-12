"""
Construa um programa onde o usuário digitará cinco números e o programa
deverá colocar esses números dentro do vetor em ordem crescente.
"""

numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

# Ordena in-place
numeros.sort()

# Imprime a lista em ordem crescente
print("\nNúmeros em ordem crescente:")

for numero in numeros:
    print(numero)
