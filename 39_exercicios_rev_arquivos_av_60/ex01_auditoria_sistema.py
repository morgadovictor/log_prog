"""
O setor de segurança da informação de uma empresa precisa rastrear as
ações dos funcionários no sistema corporativo.

i. Crie uma função em Python chamada registrar_evento(usuario, acao, status)
que receba o nome do usuário, a ação executada (ex: LOGIN, SAQUE, EXCLUSAO)
e o status da operação (SUCESSO ou FALHA).

ii. O programa deve anexar cada registro em uma nova linha no arquivo
auditoria_sistema.log, contendo a data e a hora do momento exato em que a ação
ocorreu, sem sobrescrever os registros anteriores.
"""

from datetime import datetime
from pathlib import Path

pasta = Path(__file__).parent  # pasta onde este .py está
saida_path = pasta / "auditoria_sistema.log"


def registrar_evento(usuario, acao, status):
    with open(saida_path, "w", encoding="utf-8") as saida:
        data_formatada = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        saida.write(f"{usuario}, {acao}, {status}, {data_formatada}\n")


registrar_evento("victor", "login", "success")
