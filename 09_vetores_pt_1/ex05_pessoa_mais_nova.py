"""
Construa um programa que o usuário digitará o nome e a idade de dez
pessoas e o programa escreverá o nome do usuário mais novo.
"""

# Lista que vai guardar os registros no formato [nome, idade]
pessoas = []

# Coleta dos dados: 10 pessoas
for i in range(10):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    pessoas.append([nome, idade])

# Encontra a pessoa com a MENOR idade (posição 1 do registro).
# min() devolve o registro inteiro, não só a idade.
mais_nova = min(pessoas, key=lambda x: x[1])

# Exibe apenas o nome (posição 0) da pessoa encontrada
print(f"Nome do usuário mais novo: {mais_nova[0]}")
