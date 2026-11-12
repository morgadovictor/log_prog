"""
Desenvolva um programa para registrar as vendas de uma loja ao longo
do dia. O programa deve processar múltiplos clientes até que o
operador digite 0 no total de compras para encerrar o expediente.
○ Regras de Negócio:
■ Para cada cliente, utilize um loop while que leia o valor de cada
produto comprado, somando-os até que seja digitado -1 (fim da
compra daquele cliente).
■ Se o valor total da compra for superior a R$ 200, aplique 10%
de desconto; se for superior a R$ 100, aplique 5%; caso
contrário, sem desconto (utilize if/elif/else).
■ Pergunte a quantidade de parcelas (de 1 a 6). Utilize um loop
for para exibir o cronograma de pagamento, mostrando o valor
exato de cada parcela mensal.
■ Ao final do expediente (quando for digitado 0 para novo cliente),
exiba o faturamento total acumulado do dia e a quantidade de
clientes atendidos.

○ Restrição: Utilize apenas variáveis numéricas acumuladoras (float e
int). Não utilize listas.
"""

faturamento_total = 0
quantidade_clientes = 0

while True:
    novo_cliente = int(
        input(
            "\nAtender cliente? (1 para Sim, 0 para Encerrar o expediente): "
        )
    )

    if novo_cliente == 0:
        break

    total_compra = 0
    qtd_produtos = 0

    print("\n--- Iniciando Venda ---\n")

    while True:
        compra = float(
            input(
                f"Digite o valor do {qtd_produtos + 1}º"
                "produto (ou -1 para finalizar): ",
            )
        )

        if compra == -1:
            break
        else:
            total_compra += compra
            qtd_produtos += 1

    # Guarda o subtotal antes de aplicar o desconto (para exibição)
    subtotal = total_compra

    if subtotal > 200:
        percentual_desconto = 10
        total_compra = subtotal * 0.90
    elif subtotal > 100:
        percentual_desconto = 5
        total_compra = subtotal * 0.95
    else:
        percentual_desconto = 0  # Sem desconto (total_compra segue = subtotal)

    # Soma no faturamento diário (antes de dividir pelas parcelas)
    faturamento_total += total_compra
    quantidade_clientes += 1

    print("\n--- Resumo da Compra ---")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(
        f"Desconto ({percentual_desconto}%): R$ {subtotal - total_compra:.2f}"
    )
    print(f"Total a pagar: R$ {total_compra:.2f}")

    while True:
        numero_parcelas = int(
            input("Digite a quantidade de parcelas (1 a 6): ")
        )

        if 1 <= numero_parcelas <= 6:
            break
        print("\nQuantidade inválida — escolha de 1 a 6.")

    valor_parcela = total_compra / numero_parcelas

    print("\n--- Cronograma de Pagamento ---\n")

    for parcela in range(1, numero_parcelas + 1):
        print(f"Parcela {parcela}: R$ {valor_parcela:.2f}")

print("\n" + "=" * 60)
print(f"Faturamento total acumulado do dia: R$ {faturamento_total:.2f}")
print(f"Número de clientes atendidos: {quantidade_clientes}")
print("=" * 60)
