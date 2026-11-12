"""
Construa um programa que o usuário digitará um número e a aplicação
completará o número digitado até completar cem.
"""

from sys import exit

# Entrada de dados do usuário
numero = int(input("Digite um número inteiro menor do que 100: "))

# Validação de entrada (Garante que o número é menor ou igual a 100)
if numero > 100:
    print("\nErro: O número digitado deve ser menor ou igual a 100.")
    exit()

# Contagem usando o laço For
# Inicia no número digitado, vai até 100 (incluindo) e aumenta de 1 em 1
for contador in range(numero, 101):
    print(contador)
