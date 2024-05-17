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