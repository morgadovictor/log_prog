"""
Construa um programa em Python que receba os dados para preencher
uma matriz 3x3 com números inteiros informados pelo usuário.

Após o preenchimento, o sistema deve solicitar
um valor numérico de corte (limiar).

O programa deve varrer a matriz, contabilizar quantos
elementos são estritamente maiores que esse limiar
e gerar uma segunda matriz 3x3 onde todos os valores
superiores ao limiar sejam substituídos por 0, mantendo os demais inalterados.

Ao final, exiba a contagem de elementos acima do limiar
e a matriz resultante formatada em linhas e colunas.
"""

# Cria a matriz vazia
matriz = []
nova_matriz = []
quantidade_maior = 0

# Solicita os números para o preenchimento da matriz 3x3
for i in range(3):
    linha = []

    for j in range(3):
        while True:
            try:
                numero = int(
                    input(f"\nDigite o número da posição [{i}] [{j}]: ")
                )
                break
            except ValueError:
                print("\nErro: Digite um número inteiro.")

        # Integra o número digitado em {linha}
        linha.append(numero)

    # Integra a {linha} em {matriz}
    matriz.append(linha)

# Solicita um valor numérico de corte (limiar)
while True:
    try:
        limiar = int(
            input("\nAgora digite um valor numérico de corte (limiar): ")
        )
        break
    except ValueError:
        print("\nErro: Digite um número inteiro.")

for i in range(3):
    linha = []

    for j in range(3):
        if matriz[i][j] > limiar:
            quantidade_maior += 1

# Varre a matriz e gera uma segunda matriz 3x3 onde todos os valores
# superiores ao limiar sejam substituídos por 0
for i in range(3):
    linha = []

    for j in range(3):
        # Contabiliza quantos elementos são maiores que o limiar
        if matriz[i][j] > limiar:
            quantidade_maior += 1
            # Substitui os números maiores que o limiar
            # por 0 em {nova_matriz}
            linha.append(0)
        else:  # Caso contrário integra o número [i][j] em {linha}
            linha.append(matriz[i][j])

    # Integra a {linha} em {nova_matriz}
    nova_matriz.append(linha)

print("\n", end="=" * 60)
print("\nExibição da Nova Matriz:\n")

for i in range(3):
    for j in range(3):
        print(nova_matriz[i][j], end="\t")

    print()

print(f"\nContagem de Elementos Acima do Limiar: {quantidade_maior}")
print("=" * 60)
