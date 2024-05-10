# Adição: __add__(self, other)
# Subtração: __sub__(self, other)
# Multiplicação: __mul__(self, other)
# Divisão: __truediv__(self, other)
# Divisão Inteira: __floordiv__(self, other)
# Resto da Divisão: __mod__(self, other)
# Potência: __pow__(self, other)
# E lógico: __and__(self, other)
# OU lógico: __or__(self, other)

class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __pos__(self):
        return +self.valor
    
    def __neg__(self):
        return -self.valor
    
    def __abs__(self):
        return abs(self.valor)
    
def main():
    num1 = Numero(5)
    num2 = Numero(-10)

    print("Pos = ", +num1)
    print("Neg = ", -num1)
    print("Abs = ", abs(num1))
    print("Pos = ", +num2)
    print("Neg = ", -num2)
    print("Abs = ", abs(num2))

if __name__ == "__main__":
    main()