"""
Construa um programa que só aceite notas escolares entre zero e dez
(treinamento para controle de erros).
"""

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("\nValor inválido! A nota deve estar entre 0 e 10.")

    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"\nNota registrada: {nota}")
