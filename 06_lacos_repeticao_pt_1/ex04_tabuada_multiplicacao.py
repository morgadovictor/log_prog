"""
Construa um programa onde o usuário digitará um valor e o programa
mostrará, na tela, a tabuada de multiplicação deste número.
"""

# Entrada de dados (recebe um número real)
numero = float(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}\n")

# Laço de repetição de 1 até 10 para calcular e exibir cada linha da tabuada
for i in range(1, 11):
    resultado = numero * i

    # Exibição formatada e explícita da operação
    print(f"{numero} x {i:2d} = {resultado}")
