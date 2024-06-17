class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def __str__(self):
        return f'{self.nome} : {self.idade} anos'

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    def getSalarioAnual(self):
        return self.salario * 12
    
    def __str__(self):
        return super().__str__() + '\nSalário=' + str(self.salario)
    
    def getBonificação(self):
        return self.salario * 0.10
    
class Professor(Funcionario):
    def getBonificação(self):
        return self.salario * 0.15

class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def __str__(self):
        return super().__str__()

#main
f1 = Funcionario('Josias', 26, 3000)
p1 = Professor('Malaquias', 56, 5000)
a1 = Aluno('Bruno', 26)

print( f1.getBonificação() )
print( p1.getBonificação() )
print( a1.__str__())