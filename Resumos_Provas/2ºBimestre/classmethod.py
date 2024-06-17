class Classe1:
        def metodo_objeto(self):
            return 'met instancia chamado'
        @classmethod
        def metodo_classe(cls):
            return 'met classe chamado'
        @staticmethod
        def metodo_estatico():
            return 'met estatico chamado'
obj1 = Classe1()
print( obj1.metodo_objeto())
print( Classe1.metodo_classe())
print( Classe1.metodo_estatico())