"""
A secretaria de uma escola técnica disponibilizou o arquivo notas_turma.csv
com as colunas matricula, aluno, nota1 e nota2.
i. Construa um programa em Python que leia esses registros e calcule a média
aritmética de cada aluno.
ii. Se a média final for maior ou igual a 7.0, o aluno recebe a situação
"APROVADO"; caso contrário, recebe "REPROVADO".
iii. O programa deve gerar o arquivo boletim_final.csv contendo
as notas originais, a média final arredondada para uma casa decimal
e a situação acadêmica calculada.
"""

import csv
from pathlib import Path

pasta = Path(__file__).parent  # pasta onde este .py está
entrada_path = pasta / "notas_turma.csv"
saida_path = pasta / "boletim_final.csv"


with open(entrada_path, "r", encoding="utf-8") as entrada, open(
    saida_path, "w", encoding="utf-8"
) as saida:
    leitor = csv.reader(entrada, delimiter=";")
    escritor = csv.writer(saida, delimiter=";")
    cabecalho = next(leitor)

    escritor.writerow(cabecalho + ["media", "situacao"])

    for linha in leitor:
        matricula = linha[0]
        nome = linha[1]
        nota1 = float(linha[2])
        nota2 = float(linha[3])
        media = round((nota1 + nota2) / 2, 1)
        situacao = "APROVADO" if media >= 7 else "REPROVADO"

        escritor.writerow([matricula, nome, nota1, nota2, media, situacao])
