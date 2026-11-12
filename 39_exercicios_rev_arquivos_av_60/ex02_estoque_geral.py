"""
O almoxarifado de uma assistência técnica controla suas peças por meio de
um arquivo chamado estoque_geral.csv (contendo colunas id, produto,
saldo_atual e estoque_minimo).
a. Desenvolva um script que leia esse arquivo e filtre apenas os itens cujo
saldo_atual esteja estritamente abaixo do estoque_minimo.
b. O resultado filtrado deve ser gravado em um novo arquivo chamado
pedidos_reposicao.csv, incluindo uma nova coluna calculada chamada
qtd_comprar, que representa a quantidade necessária para atingir a meta mínima.
"""

import csv
from pathlib import Path

pasta = Path(__file__).parent  # pasta onde este .py está
entrada_path = pasta / "estoque_geral.csv"
saida_path = pasta / "pedidos_reposicao.csv"


with open(entrada_path, "r", encoding="utf-8", newline="") as entrada, open(
    saida_path, "w", encoding="utf-8", newline=""
) as saida:
    leitor = csv.reader(entrada, delimiter=";")
    escritor = csv.writer(saida, delimiter=";")
    cabecalho = next(leitor)

    escritor.writerow(cabecalho + ["qtd_comprar"])

    for linha in leitor:
        id_produto = linha[0]
        produto = linha[1]
        saldo_atual = int(linha[2])
        estoque_minimo = int(linha[3])

        if saldo_atual < estoque_minimo:
            qtd_comprar = estoque_minimo - saldo_atual

            escritor.writerow(
                [id_produto, produto, saldo_atual, estoque_minimo, qtd_comprar]
            )
