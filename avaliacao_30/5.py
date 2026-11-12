"""
a. Desenvolva um módulo de console para auditar a temperatura de operação
de servidores organizados em um rack de data center. O sistema deve
gerenciar uma matriz 33, onde cada linha representa um rack físico
(Rack 0, Rack 1 e Rack 2) e cada coluna representa um sensor
de temperatura instalado (Sensor 0, Sensor 1 e Sensor 2).

i. Regras de Negócio e Requisitos:

1. O programa deve preencher a matriz 33 com as temperaturas registradas em
graus Celsius (valores do tipo float).

2. Utilize um laço while para validar individualmente a entrada de cada sensor,
aceitando apenas temperaturas contidas na faixa operacional entre 10.0C e
90.0C.

3. Para cada um dos três racks (linhas da matriz), o programa deve calcular e
exibir a temperatura média dos sensores que o compõem.

4. Identifique o ponto crítico da estrutura: descubra a maior temperatura
absoluta registrada em toda a matriz e exiba o seu valor juntamente com as
coordenadas exatas da sua localização (número do rack/linha e número do
sensor/coluna).

5. Imprima a matriz completa formatada em linhas e colunas.

6. Caso a maior temperatura absoluta encontrada seja igual ou superior a 75.0C,
exiba uma mensagem de "ALERTA: Ponto Crítico de Sobreaquecimento
Detectado".

ii. Restrição Técnica: A manipulação da matriz bidimensional deve ser realizada
por meio de laços for aninhados. É proibida a utilização de funções prontas
de biblioteca ou funções nativas de buscas (como max(), min()), sendo
obrigatória a implementação manual de acumuladores e controle condicional
de extremos. É vedado o uso de estruturas não vistas em sala.
"""

# Cria a variável {data_center}
data_center = []

# Loop para preenchimento da matriz {data_center}
for i in range(3):
    rack = []

    for j in range(3):
        # Loop While para validar a entrada de dados
        while True:
            try:
                temp = float(
                    input(f"\nDigite a temperatura do Rack {i}, Sensor {j}: ")
                )
                if 10 <= temp <= 90:
                    rack.append(temp)
                    break  # Tudo certo, sai do último Loop
                else:
                    print(
                        "\nErro: Digite uma temperatura na",
                        "faixa operacional entre 10 °C e 90 °C",
                    )
            except ValueError:
                print("\nErro: Digite um número.")

    data_center.append(rack)

# Inicializa as variáveis para uso posterior
maior_temp = data_center[0][0]
maior_temp_i = 0
maior_temp_j = 0

print()
print("=" * 60, end="")
print("\nTemperatura Média dos Sensores que Compõem:")

# Loop para mostrar as temperaturas médias dos Racks
for i in range(3):
    temp_media = 0

    for j in range(3):
        temp_media += data_center[i][j]

        if data_center[i][j] >= maior_temp:
            maior_temp = data_center[i][j]
            maior_temp_i = i
            maior_temp_j = j

    temp_media /= 3

    print(f"\nRack {i}: {temp_media:.1f} °C")

print("=" * 60)

# Mostra a localização da maior temperatura absoluta em {data_center}
print()
print("=" * 60, end="")
print("\nPonto Crítico da Estrutura:\n")
print(
    f"Maior Temperatura Absoluta: {maior_temp:.1f} °C",
    f"\nLocalização: Rack {maior_temp_i}, Sensor {maior_temp_j}",
)

# Exibe o alerta caso a maior temperatura seja maior ou igual a 75
if maior_temp >= 75:
    print("\nALERTA: Ponto Crítico de Sobreaquecimento Detectado.")

print("=" * 60)

print()
print("=" * 60, end="")
print("\nTemperatura de Operação dos Servidores do Data Center:\n")

# Loop para mostrar o dashboard do Data Center
for i in range(3):
    print(f"Rack {i}:", end="\t")
    for j in range(3):
        print(f"Sensor {j}: {data_center[i][j]} °C\t", end="")

    print()

# Exibe o alerta caso a maior temperatura seja maior ou igual a 75
if maior_temp >= 75:
    print("\nALERTA: Ponto Crítico de Sobreaquecimento Detectado.")

print("=" * 60)
