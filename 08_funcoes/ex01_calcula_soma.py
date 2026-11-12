"""
Construa um programa onde o usuário digitará dois números, utilizando
passagem de parâmetros e, dentro da função, irá calcular a soma desses
dois números.
"""


def calcula_soma(numero1, numero2):
    resultado = numero1 + numero2

    # Trata o resultado para ficar inteiro se não tiver decimais
    return int(resultado) if resultado.is_integer() else resultado


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

numero1 = int(numero1) if numero1.is_integer() else numero1
numero2 = int(numero2) if numero2.is_integer() else numero2

print(f"\nA soma de {numero1} e {numero2} é {calcula_soma(numero1, numero2)}")
