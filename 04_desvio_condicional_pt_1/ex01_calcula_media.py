"""
Construa um programa onde o usuário digitará duas notas escolares e o
programa irá calcular a média e, caso seja menor que 6, exibirá na tela:
“Aluno Reprovado”. Caso seja maior ou igual a 6 exibirá na tela: “Aluno
Aprovado”.
"""

# Solicita as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Exibe o status
if media < 6:
    print("\nAluno Reprovado.")
else:
    print("\nAluno Aprovado!")
