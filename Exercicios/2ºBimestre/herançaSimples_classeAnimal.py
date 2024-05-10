class Animal:
    def __init__(self, nome='', idade=0, peso=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def classificação(self):
        print('Classe: Animal')

    def fazerBarulho(self):
        print('Barulho: errrrrr')

    def comida(self):
        print('Comida: vegetais')

class Ave(Animal): # Herança de Animal
    def classificação(self):
        print('Classe: Ave')

    def comida(self):
        print('Comida: milho')

class Pássaro(Ave):
    def __init__(self, nome='', idade=0, peso=0.0, cor='branco'):
        super().__init__(nome, idade, peso)
        self.cor = cor

    def fazerBarulho(self):
        print('Barulho: piu piu piu')

class Mamífero(Animal):
    def __init__(self, nome='', idade=0, peso=0.0, raça=''):
        super().__init__(nome, idade, peso)
        self.raça = raça

    def classificação(self):
        print('Classe: Mamífero')

class Gato(Mamífero): # Herança de Mamífero
    def __init__(self):
        self.cor = 'branco'
        
    def fazerBarulho(self):
        print('Barulho: miau')

    def comida(self):
        print('Comida: peixe')

class Cachorro(Mamífero): # Herança de Mamífero      
    def fazerBarulho(self):
        print('Barulho: au au')

    def comida(self):
        print('Comida: ração')
        
# main
a1 = Pássaro('piu piu',cor='amarelo')
a1.classificação()
a1.fazerBarulho()
a1.comida()
print( a1.cor )

m1 = Gato()
m1.classificação()
m1.fazerBarulho()
m1.comida()

c1 = Cachorro()
c1.classificação()
c1.fazerBarulho()
c1.comida()

