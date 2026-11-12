"""
Implemente um programa que receba as temperaturas médias registradas durante
os 7 dias da semana (armazenadas em um vetor de números reais). O programa
deve calcular a média aritmética semanal e, em seguida,
exibir quais temperaturas registradas ficaram estritamente abaixo dessa média.
"""

temp_semana = []
temp_media = 0

for i in range(7):
    try:
        temp_dia = float(input(f"Digite a temperatura do {i + 1}º dia: "))

        temp_semana.append(temp_dia)
        temp_media += temp_dia
    except ValueError:
        print("\nErro: Digite apenas números.")

temp_media /= 7

print(f"\nA temperatura média da semana foi de {temp_media:.2f} °C.")
print("\nTemperaturas abaixo da média:")

for temp in temp_semana:
    if temp < temp_media:
        print(temp)
