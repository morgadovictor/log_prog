"""
Construa uma página onde o usuário digitará o nome e a média de cinco
alunos e o programa só aceitará a média
do aluno caso ela esteja entre zero e dez.
"""

# Lista que vai guardar os registros no formato [nome, média]
alunos = []

# Coleta dos dados: 5 alunos
for i in range(5):
    # O nome não precisa de validação — qualquer texto serve
    nome = input(f"Digite o nome do {i + 1}º aluno: ")

    # Loop de validação: só sai quando a média for um número E estiver
    # entre 0 e 10. Se qualquer uma das checagens falhar, repete a
    # pergunta pra esse mesmo aluno.
    while True:
        # try: captura APENAS o erro de conversão (usuário digitou
        # algo que não é número).
        try:
            media = float(input(f"Digite a média do {i + 1}º aluno: "))
        except ValueError:
            print("\nDigite uma nota válida.")
            continue  # volta pro topo do while sem tentar o if

        # Média é número válido: confere se está na faixa permitida
        if 0 <= media <= 10:
            alunos.append([nome, media])
            break  # média aceita: sai do while e vai pro próximo aluno
        else:
            print("\nA média deve estar entre 0 e 10.")
            # sem break nem continue: o while repete naturalmente
