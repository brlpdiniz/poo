class Fração:
    def __init__(self, num = 1, den = 1, calc = 0):
        self.num = num
        self.den = den
        self.calc = calc

    # mostra()
    def mostra(self):
        self.calc = self.num / self.den
        print(f'{self.num}/{self.den} = {self.calc}')

    # soma(num, num)
    def soma(self):
        self.calc = self.num + self.den
        print(f'{self.num}+{self.den} = {self.calc}')
    
    # soma(Fração, Fração)
    def soma2(self, f1, f2):
        a = f1.num
        b = f1.den
        c = f2.num
        d = f2.den
        if b == d:
            self.num = a + c
            self.den = b
        else:
            self.num = a*d + b*c
            self.den = b*d

    # toReal():double
    def toReal(self) -> float:
        return self.num/self.den

# main
f1 = Fração(5,3)
f1.mostra()
f1.soma()

f2 = Fração(10,5)
f2.mostra()
f2.soma()


f3 = Fração(100,3)
f3.mostra()
f3.soma()
