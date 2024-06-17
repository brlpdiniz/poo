class Terreste(object):
    def __init__(self, velocidade=100):
        self.se_move_em_terra = True
        self.velocidade_em_terra = velocidade

    def __str__(self):
        aux = '\nse_move_em_terra = '
        aux += str(self.se_move_em_terra)
        aux += '\nvelocidade_em_terra = '
        aux += str(self.velocidade_em_terra)
        return aux

class Aquatico(object):
    def __init__(self, velocidade=5):
        self.se_move_na_agua = True
        self.velocidade_agua = velocidade
    
    def __str__(self):
        aux = '\nse_move_na_água = '
        aux += str(self.se_move_na_agua)
        aux += '\nvelocidade_agua = '
        aux += str(self.velocidade_agua)
        return aux
#main
t1 = Terreste(110)
a1 = Aquatico(30)
print(t1)
print(a1)

class Carro(Terreste):
    def __init__(self, veloc=120, pistoes=4):
        self.rodas = 4
        self.pistoes = pistoes
        Terreste.__init__(self, veloc)
    
    def __str__(self):
        aux = '\nrodas = ' + str(self.rodas)
        aux += '\npistões = ' + str(self.pistoes)
        aux += super().__str__()
        return aux
    
class Barco(Aquatico):
    def __init__(self, veloc=6, helices=1):
        self.helices = helices
        Aquatico.__init__(self, veloc)
    
    def __str__(self):
        aux = '\nhélices = ' + str(self.helices)
        aux += super().__str__()
        return aux

class Anfibio(Carro, Barco):
    def __init__(self, vt=80, va=4, pi=6, he=2):
        Carro.__init__(self, veloc=vt, pistoes=pi)
        Barco.__init__(self, veloc=va, helices=he)
   
    def __str__(self):
        aux = Carro.__str__(self)
        aux += Barco.__str__(self)
        return aux
anf1 = Anfibio()
print(anf1)