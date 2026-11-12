"""
Construa um programa em Python que solicite 6 números inteiros ao usuário
e os armazene em uma lista. Em seguida, percorra a lista para calcular
a média aritmética de todos os valores informados
e determinar a quantidade de números pares presentes.
Ao final da execução, o programa deve exibir a lista completa,
o valor da média calculada e o total de elementos pares encontrados.
"""

# Cria uma lista vazia chamada {numeros}
numeros = []
# Cria a variável {media} para uso posterior
media = 0
# Cria a variável {quantidade_pares} para uso posterior
quantidade_pares = 0

# Loop que solicita 6 números inteiros ao usuário
for i in range(6):
    # Validação do número ser inteiro
    while True:
        try:
            numero = int(input(f"\nDigite o {i + 1}º número: "))
            break
        except ValueError:
            print("\nErro: Digite um número inteiro.")

    # Integra o número digitado na lista {numeros}
    numeros.append(numero)

# Loop que percorre a lista
for i in range(len(numeros)):
    # Adiciona todos os valores informados na variável {media}
    media += numeros[i]

    # Caso o número lido seja divisível por 2,
    # adicione 1 na variável {quantidade_pares}
    if numeros[i] % 2 == 0:
        quantidade_pares += 1

# Divide a {media} por {len(numeros)}
media /= len(numeros)

print("\n", end="=" * 30)
print("\nExibição da Lista:\n")

# Loop para exibir a lista completa
for i in range(len(numeros)):
    if i != len(numeros) - 1:
        print(numeros[i], end=" - ")
    else:
        print(numeros[i])

print(
    f"\nMédia Calculada: {media:.2f}",
    f"\nTotal de Pares Encontrados: {quantidade_pares}",
)
print("=" * 30)
