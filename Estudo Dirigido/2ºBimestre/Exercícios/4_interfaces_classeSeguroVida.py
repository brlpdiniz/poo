from abc import ABC, abstractmethod

# Definição das interfaces
class Pagador(ABC):
    @abstractmethod
    def pagarTaxa(self):
        pass

class Cobrador(ABC):
    @abstractmethod
    def cobrarTaxa(self):
        pass

# Classe base abstrata para contas
class Conta(ABC):
    def __init__(self):
        self._saldo = 0.0

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"Depositado: {valor}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor: float):
        if valor > 0:
            self._saldo -= valor
            print(f'Sacado: {valor}')
        else:
            print('Valor de saque deve ser positivo.')

    def consultar_saldo(self):
        print('Saldo: ', self._saldo)

# Implementação de Seguro Vida e Previdência Privada
class SeguroVida(Conta, Cobrador, Pagador):
    def __init__(self, valor_seguro: float):
        super().__init__()
        self._valor_seguro = valor_seguro

    def pagarTaxa(self):
        # Implementação da taxa de pagamento para Seguro de Vida (exemplo 2%)
        self._saldo += self._valor_seguro * 0.02

    def cobrarTaxa(self):
        # Implementação da taxa de cobrança para Seguro de Vida (exemplo 1%)
        self._saldo -= self._valor_seguro * 0.01

class PrevidenciaPrivada(Conta, Cobrador, Pagador):
    def __init__(self, valor_previdencia: float):
        super().__init__()
        self._valor_previdencia = valor_previdencia

    def pagarTaxa(self):
        # Implementação da taxa de pagamento para Previdência Privada (exemplo 3%)
        self._saldo += self._valor_previdencia * 0.03

    def cobrarTaxa(self):
        # Implementação da taxa de cobrança para Previdência Privada (exemplo 2%)
        self._saldo -= self._valor_previdencia * 0.02

# Testando as novas classes
if __name__ == "__main__":
    sv = SeguroVida(5000.0)
    sv.depositar(1000.0)
    sv.pagarTaxa()
    sv.cobrarTaxa()
    sv.consultar_saldo()

    pp = PrevidenciaPrivada(10000.0)
    pp.depositar(2000.0)
    pp.pagarTaxa()
    pp.cobrarTaxa()
    pp.consultar_saldo()
