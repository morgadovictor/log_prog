"""
Escreva um programa em Python que receba três valores numéricos reais (a,
b e c) representando os comprimentos dos lados de um triângulo.
◆ O programa deve primeiro verificar a condição de existência geométrica:
a soma de dois lados quaisquer deve ser estritamente maior que o
terceiro lado.
◆ Caso a condição seja atendida, classifique o triângulo em Equilátero,
Isósceles ou Escaleno.
◆ Se as medidas não formarem um triângulo, exiba uma mensagem de
erro.
"""

# Entrada de dados do usuário
lado_a = float(input("Digite o lado A: "))
lado_b = float(input("Digite o lado B: "))
lado_c = float(input("Digite o lado C: "))

# Validação de valores positivos
lados_validos = (lado_a > 0) and (lado_b > 0) and (lado_c > 0)

# Condição de existência geométrica (Desigualdade Triangular)
# A soma de dois lados deve ser estritamente maior que o terceiro
eh_triangulo = (
    (lado_a + lado_b > lado_c)
    and (lado_a + lado_c > lado_b)
    and (lado_b + lado_c > lado_a)
)

# Verificação e classificação em um único fluxo
if not lados_validos:
    print("\nErro: Todos os lados devem ser números maiores que zero.")
elif not eh_triangulo:
    print("\nErro: As medidas não formam um triângulo real.")
else:
    if lado_a == lado_b == lado_c:
        print("\nTodos os lados são iguais.")
        print("Resultado: É um triângulo equilátero.")
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
        print("\nDois lados são iguais.")
        print("Resultado: É um triângulo isósceles.")
    else:
        print("\nTodos os lados são diferentes.")
        print("Resultado: É um triângulo escaleno.")
