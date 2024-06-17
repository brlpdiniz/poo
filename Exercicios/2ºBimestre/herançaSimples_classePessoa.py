class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
   
    def getNome(self):
        return self.nome
   
    def __str__(self):
        return 'Nome = ' + self.nome + '\nIdade = ' + str(self.idade)
 
class Funcionário(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
   
    def getSalario(self):
        return self.salario
 
    def getSalarioAnual(self):
        return self.salario * 12
   
    def __str__(self):
        return super().__str__() + '\nSalário = ' + str(self.salario)
 
    def getBonificação(self):
        return self.salario * 0.10
 
class Professor(Funcionário):
    def getBonificação(self):
        return self.salario * 0.15
 
# main
f1 = Funcionário('Josias', 26, 3000)
p1 = Professor('Malaquias', 56, 500)