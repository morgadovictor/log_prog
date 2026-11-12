"""
a. Desenvolva um sistema de console para auditar o consumo elétrico
de maquinários em uma linha de produção industrial.

O sistema deve monitorar 5 máquinas utilizando vetores unidimensionais.

i. Regras de Negócio e Requisitos:

1. O programa deve preencher duas listas paralelas de tamanho fixo (5
posições): uma contendo o código numérico de identificação de cada
máquina e outra contendo o respectivo consumo registrado em quilowatt-
hora (kWh).

2. Para cada máquina, o sistema deve validar a entrada do consumo através de
um laço while, garantindo que o valor informado em kWh seja estritamente
maior que zero antes de passar para a máquina seguinte.

3. Solicite ao operador o valor do "Teto Operacional de Consumo" (número real
único para a verificação de toda a linha industrial).

4. Realize uma varredura nas estruturas e identifique:
a. Quais máquinas ultrapassaram o teto operacional, exibindo seu
código e o consumo registrado;
b. O código e o consumo da máquina com o maior consumo absoluto da
planta;
c. A média aritmética de consumo de todas as 5 máquinas.
"""

cod_numerico = []
consumos = []

# Loop que solicita 6 números inteiros ao usuário
for i in range(5):
    # Validação do número ser inteiro
    while True:
        try:
            cod_numerico.append(
                input(f"\nDigite o código númerico da {i + 1}º máquina: ")
            )
            break
        except ValueError:
            print("\nErro: Digite um número inteiro.")

    while True:
        try:
            consumo = float(input(f"Digite o consumo da {i + 1}º máquina: "))

            # Garante que a > 0
            if consumo > 0:
                consumos.append(consumo)
                break
            else:
                print("\nErro: Digite um valor maior do que 0.")
        except ValueError:
            print("\nErro: Digite um número inteiro.")

teto_consumo = float(
    input("\nDigite o valor do Teto Operacional de Consumo: ")
)

maior_consumo = consumos[0]
maior_consumo_cod = cod_numerico[0]
media_consumos = 0

print("\n", end="=" * 60)
print("\nMáquinas que Ultrapassaram o Teto Operacional:\n")

for i in range(len(consumos)):
    media_consumos += consumos[i]

    if consumos[i] > maior_consumo:
        maior_consumo = consumos[i]
        maior_consumo_cod = cod_numerico[i]

    if consumos[i] > teto_consumo:
        print(
            f"Código númerico: {cod_numerico[i]}",
            f"\nConsumo: {consumos[i]:.2f} kWh\n",
        )

media_consumos /= len(consumos)

print("=" * 60)
print("\n", end="=" * 60)
print(
    "\nCódigo e o Consumo da Máquina com o Maior Consumo Absoluto da Planta:\n"
)
print(f"Código: {maior_consumo_cod}\nConsumo: {maior_consumo:.2f} kWh")
print("=" * 60)

print("\n", end="=" * 60)
print("\nMédia Aritmética de Consumo de Todas as 5 Máquinas:\n")
print(f"Média: {media_consumos:.2f} kWh")
print("=" * 60)
