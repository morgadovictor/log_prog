"""
Crie um script que avalie a concessão de empréstimo com base em três
variáveis: renda_mensal (float), score (inteiro de 0 a 1000) e possui_restricao
(booleano).
◆ Aprovado: score maior ou igual a 700, renda_mensal a partir de 4000.00
e sem restrições cadastrais.
◆ Análise Manual: Se não for aprovado diretamente, mas a renda_mensal
for de pelo menos 2500.00, sem restrições, e (score maior ou igual a 500
ou renda_mensal superior a 6000.00).
◆ Recusado: Qualquer outro caso.
"""

import random
from sys import exit

# Entrada de dados (solicita e valida a renda do usuário)
renda_mensal = float(input("Digte sua renda mensal: "))

# Validação para garantir que a renda seja positiva
if renda_mensal <= 0:
    print("\nErro: A renda mensal deve ser um valor positivo.")
    exit()

# Simulação das variáveis de score e restrição cadastral
score = random.randint(0, 1000)  # Pontuação de 0 a 1.000
possui_restricao = random.choice([True, False])

# Exibição dos dados do perfil gerado
if possui_restricao:
    print(f"\nSeu score é {score}, e você possui restrição de crédito.")
else:
    print(f"\nSeu score é {score}, e você não possui restrição de crédito.")

# 1. Condição para Aprovação Direta
# Score >= 700, Renda >= 4000.00 e Sem Restrições
if (score >= 700) and (renda_mensal >= 4000) and not possui_restricao:
    print("\nResultado: Aprovado.")
# 2. Condição para Análise Manual
# Sem restrições E Renda >= 2500.00 E (Score >= 500 OU Renda > 6000.00)
elif (
    not possui_restricao
    and renda_mensal >= 2500
    and (score >= 500 or renda_mensal > 6000)
):
    print("\nResultado: Encaminhado para a Análise Manual.")
# 3. Qualquer outro caso resulta em recusa
else:
    print("\nResultado: Recusado.")
