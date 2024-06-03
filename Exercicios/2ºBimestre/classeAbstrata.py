from abc import ABC, abstractmethod
import math
 
class Poligono(ABC):
 
    @abstractmethod
    def area(self):
        pass
 
    @abstractmethod
    def perimetro(self):
        pass
 
    @abstractmethod
    def diametro(self):
        pass
 
    def __str__(self):
        aux = f"Area: {self.area()}"
        aux += f"\nPerimetro: {self.perimetro()}"
        aux += f"\nDiametro: {self.diametro()}"
        return aux
 
class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
 
    def area(self):
        return self.lado ** 2
       
    def perimetro(self):
        return self.lado * 4
 
    def diametro(self):
        return self.lado * math.sqrt(2)
 
   
q1 = Quadrado(5)
print(q1)
 
class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio
 
    def area(self):
        return (self.raio ** 2) * 3.14
 
    def perimetro(self):
        return self.raio * 2 * 3.14
 
    def diametro(self):
        return self.raio ** 2
 
   
C1 = Circulo(5)
print(C1)
 
class Retangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
 
    def area(self):
        return self.base * self.altura
 
    def perimetro(self):
        return 2 * (self.base + self.altura)
 
    def diametro(self):
        return math.sqrt(self.base**2 + self.altura**2)
 
R1 = Retangulo(5,8)
print(R1)