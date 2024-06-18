class Conta:
    def __init__(self, nome = '', codigo = int, valor = float):
        self.nome = nome
        self.codigo = codigo
        self.saldo = valor
    
    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print(f'Depósito de R$ {valor:.2f} realizado!')

    def saque (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado!')
        else:
            print ('Você não tem saldo o suficiente!')

    def consultar_saldo(self):
        print(f'O seu saldo é de R$ {self.saldo:.2f}!\n')
    
    def transferencia(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.deposito(valor)
            print(f'R$ {valor:.2f} enviado para {conta_destino.nome}!')
        else:
            print ('Você não tem saldo o suficiente!')

class contaCorrente(Conta):
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)
        self.limite = 700

    def saque(self, valor):
        if valor > self.saldo or valor > self.limite:
            print('Não é possível realizar o saque!')
            print('Saldo insuficiente ou o valor ultrapassou R$  700,00 !')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado!')

class contaEspecial(Conta):
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)
    
    def limiteEspecial(self, valor):
        if self.saldo < valor:
            print('Você não tem saldo o suficiente')
            print('Sua conta entrará no cheque especial')
            taxa = valor * 0.05
            self.saldo -= valor + taxa
            print(f'Seu novo saldo é de R$  {self.saldo}!')

class contaPoupança(Conta):
    def __init__(self, nome = '', codigo = int, valor = float):
        super().__init__(nome, codigo, valor)

    def saque(self, valor):
        if valor > self.saldo:
            print('Não é possível realizar o saque!')
            print('Saldo insuficiente ou o valor ultrapassou R$  700,00 !')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado!')
    
    def reajusteMensal(self):
        inflacao = 0.0
        reajuste = self.saldo * (inflacao + 0.005)
        self.saldo += reajuste
        print(f'Reajustado! Seu saldo é de R$ {self.saldo}')

def main():
    conta_corrente1 = contaCorrente('Bruno', 1, 1000.0)
    conta_corrente1.deposito(500.0)
    conta_corrente1.saque(300.0)
    conta_corrente1.transferencia(200.0, Conta('Gustavo', 2, 100.0))
    conta_corrente1.consultar_saldo()

    conta_especial1 = contaEspecial('Bonetto', 3, 1500.0)
    conta_especial1.limiteEspecial(2000.0)
    conta_especial1.limiteEspecial(500.0)
    conta_especial1.consultar_saldo()

    conta_poupanca = contaPoupança('Fillipe', 4, 10.0)
    conta_poupanca.deposito(1000.0)
    conta_poupanca.reajusteMensal()
    conta_poupanca.saque(500.0)
    conta_poupanca.consultar_saldo()

if __name__ == '__main__':
    main()