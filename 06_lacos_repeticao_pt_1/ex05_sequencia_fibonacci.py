"""
Construa um programa que exiba a sequência de Fibonacci de zero até dois
mil.
"""

a, b = 0, 1  # os dois primeiros termos da sequência

# Laço executa enquanto o termo atual for menor ou igual a 2000
while a <= 2000:
    print(a)

    a, b = b, a + b  # avança: a vira o próximo termo, b vira a soma
