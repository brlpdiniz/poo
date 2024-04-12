import math

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distancia(self, outro_ponto):
        dx = outro_ponto.x - self.x
        dy = outro_ponto.y - self.y
        return math.sqrt(dx**2 + dy**2)

#main
ponto1 = Ponto(1,2)
ponto2 = Ponto(4,6)
print("Distância entre os pontos: ", ponto1.distancia(ponto2))