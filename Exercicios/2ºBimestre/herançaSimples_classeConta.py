class Conta:
    def __init__(self, nome = '', codigo = int, valor = float):
        self.nome = nome
        self.codigo = codigo
        self.saldo = valor
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado!')

    def saque (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado!')
        else:
            print ('Você não tem saldo o suficiente!')

    def saldo(self):
        print(f'O seu saldo é de R${self.saldo}!')
    
    def transferencia(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.deposito(valor)
            print(f'R${valor:.2f} enviado para {conta_destino.nome}!')
        else:
            print ('Você não tem saldo o suficiente!')

class contaCorrente(Conta):
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)
        self.limite = 700

    def saque(self, valor):
        if valor > self.saldo and valor > self.limite:
            print('Não é possível realizar o saque!')
            print('Saldo insuficiente ou o valor ultrapassou R$ 700,00 !')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado!')

class contaEspecial(Conta):
    def 


class contaPoupança(Conta):
    def 