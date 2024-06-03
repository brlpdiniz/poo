# ------------------------------- CLASSE NÃO ABSTRATA ------------------------------- #
class Conta:
    def __init__(self):
        self.saldo = 0.0
    
    def saque(self, valor):
        if valor <= 0.0:
            print ("Você não tem saldo o suficiente!")
        else:
            self.saldo -= valor
            print ("Saque realizado com sucesso!")
    
    def deposito(self, valor):
        if valor <= 0.0:
            print ("Valor incorreto para depósito")
        else:
            self.saldo += valor
            print ("Depósito realizado com sucesso!")
    
    def saldo(self):
        return f"{self.saldo}"

#main
c = Conta()
c.deposito(100)
c.saque(2100)
c.saldo()
    

# ------------------------------- CLASSE ABSTRATA ------------------------------- #
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self):
        self.saldo = 0.0
    
    @abstractmethod
    def saque(self, valor):
        if valor <= 0.0:
            print ("Você não tem saldo o suficiente!")
        else:
            self.saldo -= valor
            print ("Saque realizado com sucesso!")
    
    @abstractmethod
    def deposito(self, valor):
        if valor <= 0.0:
            print ("Valor incorreto para depósito")
        else:
            self.saldo += valor
            print ("Depósito realizado com sucesso!")
    
    @abstractmethod
    def saldo(self):
        return f'{self.saldo}'

# Interface (Decorador)
class Pagador(ABC):

    @abstractmethod
    def pagarTaxa(self):
        pass

# Interface (Decorador)
class Cobrador(ABC):

    @abstractmethod
    def cobrarTaxa(self):
        pass

class ContaPoupança(Conta):
    def saque(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            super().saque(valor) # chamada classe Conta 
    
    def pagarTaxa(self):
        # 0.5% ao mes
        self.saldo += self.saldo * 0.005

    def cobrarTaxa(self):
        # isenta
        pass

class ContaCorrente(Conta):
    def saque(self, valor):
        if valor > 700.0:
            print('Valor diário excedido para saque!')
        elif valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            super().saque(valor) # chamada classe Conta
    
    def pagarTaxa(self):
        # nao paga
        pass

    def cobrarTaxa(self):
        self.saldo -= 30.0

#main
d = ContaCorrente()
d.saque(701.0)
d.saque(500.0)