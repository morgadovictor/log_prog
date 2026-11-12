"""
Construa um programa onde o usuário digitará dez números. O programa
deverá calcular quais deles são maiores que dez.
"""

# Lê os 10 números via list comprehension:
# cada iteração chama input() e converte para int na hora
numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(10)]

# Filtra só os maiores que 10 (note: "maior que 10" é > 10, não >= 10;
# o 10 em si não entra na lista, conforme o enunciado)
numeros_maiores_10 = [n for n in numeros if n > 10]

# Se a lista filtrada não estiver vazia, mostra os números; senão,
# avisa que nenhum passou do critério (evita imprimir cabeçalho "solto")
if numeros_maiores_10:
    print("\nNúmeros digitados maiores que 10:")

    for numero in numeros_maiores_10:
        print(numero)
else:
    print("\nNão há número maior que 10.")
