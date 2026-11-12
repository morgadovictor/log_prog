"""
Construa um programa onde o usuário digitará o nome e a média de dez
alunos e o programa escreverá, na tela, o nome de todos com a média acima
ou igual a seis.
"""

# Lista que vai guardar os registros no formato [nome, média]
registro = []

# Coleta dos dados: 10 alunos
for i in range(10):
    aluno = input(f"Digite o nome do {i + 1}º aluno: ")
    media = float(input(f"Digite a média do {i + 1}º aluno: "))
    registro.append([aluno, media])

# Filtra os alunos com média >= 6 e já extrai só o nome (posição 0).
# A condição usa a média (posição 1) para decidir quem entra na lista.
nomes = [aluno[0] for aluno in registro if aluno[1] >= 6]

# Se a lista não estiver vazia, mostra os nomes; senão, avisa que
# ninguém atingiu a média (evita imprimir um cabeçalho "solto")
if nomes:
    print("\nAlunos com a média maior ou igual a 6:")

    for nome in nomes:
        print(nome)
else:
    print("\nNenhum aluno atingiu a média.")
