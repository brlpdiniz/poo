import math

class NumerosComplexos:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imaginario = imag

    def __str__(self):
        return f'{self.real:.2f} + {self.imaginario:.2f}i'

    def inverso(self):
        return NumerosComplexos(-self.real, -self.imaginario)

    def conjugado(self):
        return NumerosComplexos(self.real, -self.imaginario)

    def __add__(self, other):
        return NumerosComplexos(self.real + other.real, self.imaginario + other.imaginario)

    def __sub__(self, other):
        return self + other.inverso()

    def __mul__(self, other):
        real = self.real * other.real - self.imaginario * other.imaginario
        imag = self.real * other.imaginario + self.imaginario * other.real
        return NumerosComplexos(real, imag)

    def __truediv__(self, other):
        conj = other.conjugado()
        numerador = self * conj
        denominador = other.real**2 + other.imaginario**2
        real = numerador.real / denominador
        imag = numerador.imaginario / denominador
        return NumerosComplexos(real, imag)

    def __eq__(self, other):
        return self.real == other.real and self.imaginario == other.imaginario

    def distancia(self, other):
        return math.sqrt((self.real - other.real)**2 + (self.imaginario - other.imaginario)**2)

    def ponto_medio(self, other):
        return NumerosComplexos((self.real + other.real) / 2, (self.imaginario + other.imaginario) / 2)

    def modulo(self):
        return math.sqrt(self.real**2 + self.imaginario**2)

    def angulo(self):
        return math.atan2(self.imaginario, self.real)


# main
c1 = NumerosComplexos(5, 8)
c2 = NumerosComplexos(3, -4)

print(f'Número complexo c1: {c1}')
print(f'Conjugado de c1: {c1.conjugado()}')
print(f'Inverso de c1: {c1.inverso()}')
print(f'Soma de c1 e c2: {c1 + c2}')
print(f'Subtração de c1 e c2: {c1 - c2}')
print(f'Multiplicação de c1 e c2: {c1 * c2}')
print(f'Divisão de c1 por c2: {c1 / c2}')
print(f'c1 é igual a c2? {"Sim" if c1 == c2 else "Não"}')
print(f'Distância entre c1 e c2: {c1.distancia(c2)}')
print(f'Ponto médio entre c1 e c2: {c1.ponto_medio(c2)}')
print(f'Módulo de c1: {c1.modulo()}')
print(f'Ângulo de c1: {math.degrees(c1.angulo())} graus')
