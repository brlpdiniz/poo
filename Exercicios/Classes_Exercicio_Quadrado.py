import math

class Quadrado:
    def __init__(self, lado = int):
        self.lado = lado
    
    # area():double
    def area(self) -> float:
        return self.lado ** 2

    # perimeto():double
    def perimetro(self) -> float:
        return self.lado * 4

    # diagonal():double
    def diagonal(self) -> float:
        return self.lado * math.sqrt(2)

    # mostra():double
    def mostra(self):
        print('Área: ', self.area())
        print('Perímetro: ', self.perimetro())
        print('Diagonal: ', self.diagonal())

# main
f1 = Quadrado(10)
f1.mostra()