"""
Um sistema de controle de maquinário pesado deve autorizar a operação
com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
◆ A chave_emergencia estiver ativa (True), independentemente de
qualquer outra variável; OU
◆ O usuário for "supervisor"; OU
◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".
"""

import random
from sys import exit

# Simulação das variáveis do sistema
hora_atual = random.randint(0, 23)
minuto_atual = random.randint(0, 59)
chave_emergencia = random.choice([True, False])

print(f"Hora atual: {hora_atual:02d}:{minuto_atual:02d}")

# Entrada do cargo do usuário (normalizada para minúsculas, sem espaços)
cargo = input("Digite o seu cargo (operador/supervisor): ").strip().lower()

# Validação simples do cargo digitado
if cargo not in ["operador", "supervisor"]:
    print("\nErro: Cargo inválido. Escolha entre 'operador' ou 'supervisor'.")
    exit()

# Avaliação do acesso
acesso_concedido = (
    chave_emergencia
    or cargo == "supervisor"
    or (cargo == "operador" and 8 <= hora_atual <= 17)
)

# Exibição do contexto e do resultado
if chave_emergencia:
    print("\nA chave de emergência está ativada.")
else:
    print("\nA chave de emergência está desativada.")

print(f"Cargo informado: {cargo.capitalize()}")

if acesso_concedido:
    print("Acesso concedido.")
else:
    print("Acesso bloqueado.")
