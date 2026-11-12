"""
Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
em seguida, solicite um número adicional para consulta.
O sistema deve verificar e exibir se esse valor está presente no vetor
e a quantidade exata de vezes que ele se repete.
"""

# Cria a variável {lista}
lista = []

# Laço de repetição que solicita e armazena os 10 n. inteiros na lista
for i in range(10):
    while True:
        try:
            lista.append(int(input(f"Digite o {i + 1}º número: ").strip()))
            break
        except ValueError:
            print("\nErro: Digite apenas valores inteiros.")

# Cria a variável {numero_consulta}
numero_consulta = int(
    input("\nAgora digite um número para consultar na lista: ").strip()
)

# Verifica se o número consultado está presente na lista
if numero_consulta in lista:
    print(
        f"\nO número consultado ESTÁ presente {lista.count(numero_consulta)}",
        "vez(es) na lista.",
    )
# Caso contrário, não está presente
else:
    print("\nO número consultado NÃO está presente na lista.")
