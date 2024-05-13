class Conta:
    def __init__(self, nome = '', codigo = int, valor = float):
        self.nome = nome
        self.codigo = codigo
        self.saldo = valor
    
    def deposito(self, valor):
        self.saldo = self.saldo + valor
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
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)
    
    def limiteEspecial(self, valor):
        if self.saldo < valor:
            print('Você não tem saldo o suficiente')
            print('Sua conta entrará no cheque especial')
            aux = valor * 0.05
            self.saldo -= valor + aux
            print(f'Seu novo saldo é de {self.saldo}!')

class contaPoupança(Conta):
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)

    def saque(self, valor):
        if valor > self.saldo:
            print('Não é possível realizar o saque!')
            print('Saldo insuficiente ou o valor ultrapassou R$ 700,00 !')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado!')
    
    def reajusteMensal(self, valor):
        aux = self.saldo * 0.005
        self.saldo += aux
        print(f'Seu saldo é de {self.saldo}')

#main
saldo1 = contaPoupança('Bruno', 2.5, 89.50)
saldo2 = saldo1.reajusteMensal(100)
saldo3 = saldo1.saldo(50)