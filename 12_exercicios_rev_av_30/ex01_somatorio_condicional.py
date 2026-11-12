"""
Desenvolva um programa que solicite dois números inteiros representando os
limites de um intervalo [A, B] (garantindo que A ≤ B).
O programa deve iterar sobre o intervalo utilizando uma estrutura de repetição
e calcular a soma apenas dos números ímpares presentes nele,
exibindo o resultado final ao usuário.
"""


# Função que retorna a soma dos n. ímpares presentes no intervalo
def soma_impares_intervalo(a, b):
    # Cria a variável {soma}
    soma = sum(i for i in range(a, b + 1) if i % 2 != 0)
    return soma


# Solicita o limite A do intervalo.
while True:
    try:
        a = int(input("Digite A do intervalo [A, B]: ").strip())
        break
    except ValueError:
        print("\nErro: Digite apenas valores inteiros.")

# Solicita o limite B do intervalo.
while True:
    try:
        b = int(input(f"Digite B do intervalo [{a}, B]: ").strip())

        # Garante que A ≤ B
        if a > b:
            print(
                f"\nErro: B não pode ser menor que A ({a}). Tente novamente."
            )
        else:
            break  # Se estiver tudo certo, sai do loop
    except ValueError:
        print("\nErro: Digite apenas valores inteiros.")

# Exibe o resultado
print(
    f"\nResultado da soma apenas dos números ímpares presentes em [{a}, {b}]",
    f"é: {soma_impares_intervalo(a, b)}",
)
