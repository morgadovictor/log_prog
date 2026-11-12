"""
Construa um programa onde o usuário digitará sete números e o programa
escreverá, na tela, quantos deles são pares e quantos são ímpares.
"""

# Lê os 7 números de uma vez via list comprehension:
# cada iteração chama input() e converte para int na hora
numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(7)]

# Conta os pares: para cada número par (resto da divisão por 2 == 0),
# o generator interno gera 1; o sum() soma esses 1s e devolve o total
pares = sum(1 for n in numeros if n % 2 == 0)

print(f"\nTotal de números pares: {pares}")

# Ímpares = total - pares. Funciona porque todo inteiro é par OU ímpar,
# então não precisa percorrer a lista de novo contando os ímpares
print(f"Total de números ímpares: {len(numeros) - pares}")
