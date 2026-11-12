"""
Desenvolva um módulo de console para auditar o consumo de combustível de
veículos que retornam à base operacional ao longo de um turno de trabalho.
● Regras de Negócio e Requisitos:
1. O programa deve processar múltiplos veículos de forma contínua até
que o operador digite 0 na quilometragem percorrida para sinalizar o
fim do expediente.
2. Para cada veículo válido, solicite a distância percorrida (em km) e a
quantidade de combustível consumida (em litros). Utilize um laço while
para validar que o volume de combustível seja estritamente maior que
zero antes de prosseguir com o cálculo.
3. Calcule o consumo médio (km/l) e classifique o desempenho do
veículo:
■ Consumo maior ou igual a 12. 0km/l: "Econômico";
■ Consumo entre 9. 0km/l e 11. 9km/l: "Padrão";
■ Consumo inferior a 9. 0km/l: "Alto Consumo".
4. Exiba a classificação do veículo processado.
5. Ao encerrar o expediente, exiba:
■ O total de veículos auditados;
■ A quilometragem total acumulada pela frota;
■ A média geral de consumo da frota no turno.

● Restrição Técnica: O processamento deve utilizar unicamente
acumuladores e variáveis numéricas primitivas (float e int), sem o uso de
listas ou estruturas compostas.
"""

total_veiculos = 0
quilometragem_total = 0
combustivel_total = 0

while True:
    # Solicita a distância percorrida
    quilometragem = float(
        input("\nDigite a distância percorrida (em km): ").strip()
    )

    if quilometragem == 0:
        break

    # Guarda quilometragem total para uso posterior
    quilometragem_total += quilometragem

    while True:
        # Solicita a quantidade de combustível consumida
        combustivel = float(
            input(
                "Digite a quantidade de combustível consumida (em litros): "
            ).strip()
        )

        # Valida que o volume de combustível é maior que 0
        if combustivel > 0:
            break

    # Guarda combustível geral para uso posterior
    combustivel_total += combustivel
    # Calcula o consumo médio (km/l)
    consumo = quilometragem / combustivel
    # Guarda o total de veículos
    total_veiculos += 1

    print(f"\nConsumo médio (km/l): {consumo:.2f}")

    # Classifica o desempenho do veículo
    if consumo >= 12:
        print("Classificação de desempenho do veículo: Econômico.")
    elif 9 <= consumo < 12:
        print("Classificação de desempenho do veículo: Padrão.")
    else:
        print("Classificação de desempenho do veículo: Alto Consumo.")

if total_veiculos > 0:
    print(
        "\nResumo:",
        f"\nTotal de veículos auditados: {total_veiculos}"
        "\nQuilometragem total acumulada pela frota: ",
        f"{quilometragem_total:.0f}",
        "\nMédia geral de consumo da frota no turno: ",
        f"{quilometragem_total / combustivel_total:.2f}",
    )
