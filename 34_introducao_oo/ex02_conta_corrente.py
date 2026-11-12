from ex01_conta import Conta


class ContaCorrente(Conta):
    """
    Subclasse que especializa a Conta
    """

    def __init__(
        self, nome, conta, agencia=2, saldo=0.0, taxa_saque=6.5
    ) -> None:
        super().__init__(nome, conta, agencia, saldo)
        self._taxa_saque = taxa_saque

    def realizar_saque(self, valor):
        if valor <= 0:
            print("\nDigite um valor de saque válido.")
            return False

        custo_total = valor + self._taxa_saque

        if self._saldo < custo_total:
            print("\nVocê não tem saldo suficiente.")
            return False

        # self._saldo -= valor + custo_total
        # return True

        novo_saldo = self.saldo - custo_total
        self._extrato.append(
            f"Saque: -R$ {valor:.2f} (Taxa: R$ {self._taxa_saque:.2f}) | "
            f"Saldo: R$ {self._saldo:.2f}"
        )
        self.saldo = novo_saldo
        return True


conta_Lucia = ContaCorrente("Lúcia", 1, 2, 150)
conta_Lucia.realizar_saque(50)
conta_Lucia.exibir_extrato()
