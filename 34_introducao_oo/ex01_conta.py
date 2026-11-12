"""
Vamos  criar  um  sistema  bancário  com  saque,  depósito,  extrato,
transferência.
"""


class Conta:
    def __init__(self, nome, conta, agencia=1, saldo=0.0) -> None:
        self._nome = nome
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo
        self._extrato = []

        if self._saldo > 0:
            self._extrato.append(f"Depósito inicial: +R$ {self._saldo:.2f}")

    # def get_saldo(self):
    #     return self._saldo

    # def set_saldo(self, novo_saldo):
    #     if novo_saldo >= 0:
    #         self._saldo = novo_saldo
    #         return True
    #     else:
    #         print("\nSaldo não pode ser negativo.")
    #         return False

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("\nSaldo não pode ser negativo.")

        self._saldo = novo_saldo

    def realizar_saque(self, valor):
        if valor <= 0:
            print("\nDigite um valor de saque válido.")
            return False

        if self._saldo < valor:
            print("\nVocê não tem saldo suficiente.")
            return False

        self._saldo -= valor
        self._extrato.append(
            f"Saque: -R$ {valor:.2f} | Saldo: R$ {self._saldo:.2f}"
        )
        return True

    def realizar_deposito(self, valor):
        if valor <= 0:
            print("\nDigite um valor de depósito válido.")
            return False

        self._saldo += valor
        self._extrato.append(
            f"Depósito: +R$ {valor:.2f} | Saldo: R$ {self._saldo:.2f}"
        )
        return True

    def realizar_transferencia(self, conta_destino, valor):
        if not self.realizar_saque(valor):
            print("\nA transferência não pôde ser realizada.")
            return False

        if not conta_destino.realizar_deposito(valor):
            self.realizar_deposito(valor)  # estorna o saque
            print("\nA transferência foi revertida.")
            return False
        return True

    def exibir_extrato(self):
        print("\n--- Dados ---")
        print(f"Titular: {self._nome}")
        print(f"Conta:   {self._conta}")
        print(f"Agência:   {self._agencia}")
        print(f"Saldo:   R$ {self._saldo:.2f}")
        print("\n--- Histórico ---")

        if not self._extrato:
            print("Nenhuma transação realizada.")
        else:
            for linha in self._extrato:
                print(linha)


class ContaPoupanca(Conta):

    def __init__(
        self, nome, conta, agencia=20, saldo=0.0, rendimento=0.005
    ) -> None:
        super().__init__(nome, conta, agencia, saldo)
        self._rendimento = rendimento

    def render_juros(self):
        juros = self._saldo * self._rendimento
        self._saldo += juros
        self._extrato.append(
            f"Rendimento: +R$ {juros:.2f} | Saldo: R$ {self._saldo:.2f}"
        )


if __name__ == "__main__":
    conta_Victor = Conta("Victor", 1, 1, 100)

    conta_Victor.exibir_extrato()

    print(conta_Victor.saldo)

    conta_Leda = ContaPoupanca("Leda", 2, 20, 1000, 0.01)

    conta_Leda.exibir_extrato()
    conta_Leda.realizar_saque(100)

    print(conta_Leda.saldo)

    conta_Victor.realizar_transferencia(conta_Leda, 150)
    conta_Victor.realizar_transferencia(conta_Leda, 30)

    conta_Leda.render_juros()
    conta_Leda.exibir_extrato()
