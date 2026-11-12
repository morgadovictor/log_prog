"""
Construa um programa onde o usuário digitará três números e o programa
exibirá, na tela, o maior entre eles.
"""

# Solicita três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

# Exibe o maior entre eles
print(f"\nO maior número é: {maior}")
