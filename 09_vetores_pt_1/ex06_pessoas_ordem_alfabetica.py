"""
Construa uma página/programa onde o usuário digitará o nome e o bairro de
dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
alfabética.
"""

# Lista que vai guardar os registros no formato [nome, bairro]
pessoas = []

# Coleta dos dados: 10 pessoas
for i in range(10):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    bairro = input(f"Digite o bairro da {i + 1}ª pessoa: ")
    pessoas.append([nome, bairro])

# Ordena a lista: primeiro pelo bairro (x[1]), depois pelo nome (x[0])
# como critério de desempate — assim, pessoas do mesmo bairro ficam em
# ordem alfabética entre si
pessoas.sort(key=lambda x: (x[1], x[0]))

# Exibe nome e bairro de cada pessoa já ordenada
for i in range(len(pessoas)):
    print(pessoas[i][0], " | ", pessoas[i][1])
