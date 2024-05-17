# Exemplo 1
class Bebida:
    nome = "Bebida"     # atributo da classe

    @classmethod
    def imprimir_nome(cls):
        print(f"Esta bebida é do tipo {cls.nome}")


class Café(Bebida):
    nome = "Café"


class Chá(Bebida):
    nome = "Chá"


#main
Bebida.imprimir_nome()
Café.imprimir_nome()
Chá.imprimir_nome()


# Exemplo 2
class Informativo:
    mensagem1 = "Primeira Aula!"

    @classmethod
    def printar(cls):
        print(f'Informativo: {cls.mensagem1}')

#main
obj1 = Informativo()
obj2 = Informativo()
obj3 = Informativo()

obj1.printar()
obj2.printar()
obj3.printar()

Informativo.mensagem1 = 'Segunda Aaula!'
obj1.printar()
obj2.printar()
obj3.printar()


# Método Estático (Exemplo 3)
class Calculadora:
    @staticmethod
    def somar(x, y):
        return x + y
    
    @staticmethod
    def subtrair(x, y):
        return x - y

#main
print(Calculadora.somar(5, 3))
print(Calculadora.subtrair(60, 15))


# Exemplo 4
class Classe1:
    def metodo_objeto(self):
        return 'metodo de instância chamado', self
    
    @classmethod
    def metodo_classe(cls):
        return 'metodo de classe chamado', cls
    
    @staticmethod
    def metodo_estatico():
        return 'metodo estático chamado'

obj1 = Classe1()
print( obj1.metodo_objeto() )

print( Classe1.metodo_classe() )
print ( Classe1.metodo_estatico() )


# Exemplo de como 
from abc import ABC, abstractclassmethod

class Abstrata(ABC):
    numero = 10

    @abstractclassmethod
    def mostra(self):
        print('nao deu')

# main (comentado pq dá erro (erro está certo pq a classe é abstrata))
# obj1 = Abstrata()
# obj1.mostra()


# Exemplo 5
class Veículo(ABC):
    @abstractclassmethod
    def Número_portas(self):
        pass

    def Motor(self):
        print("Flex")


class Carro(Veículo):
    def Número_portas(self):
        print("Quatro")


class Moto(Veículo):
    def Número_portas(self):
        print("Duas")

# main
carro1 = Carro()
carro1.Motor()
carro1.Número_portas()

moto1 = Moto()
moto1.Motor()
moto1.Número_portas()