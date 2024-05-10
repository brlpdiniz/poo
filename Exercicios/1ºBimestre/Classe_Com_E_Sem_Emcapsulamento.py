# ---------------------------------------- CLASSE SEM ENCAPSULAMENT -------------------------------------------------
class Produto1:
    def __init__(self, preço):
        self.preço = preço

#main
obj = Produto1(500)
print(obj.preço)

obj = Produto1(1000)
print(obj.preço)



# ---------------------------------------- CLASSE COM ENCAPSULAMENT -------------------------------------------------
class Produto2:
    def __init__(self, preço):
        self.preço = preço

    def getPreço(self):
        return self.preço
    
    def setPreço(self, valor):
        self.preço = valor

#main
obj = Produto2(500)
print(obj.getPreço())

obj = Produto2(1000)
print(obj.getPreço())



# ---------------------------------------- CLASSE COM PROPRIEDADES -------------------------------------------------
class Produto3:
    def __init__(self, preço):
        self.preço = preço

    @property
    def preço(self):
        return self.preço
    
    @preço.setter
    def preço(self, novo):
        if novo > 0 and isinstance(novo, float):
            self.preço = novo
        else:
            print("Insira um preço válido (positivo)")
    
    @preço.deleter
    def preço(self):
        del self.preço

#main
obj = Produto3(500)
print(obj.preço)

obj = Produto3(1000)
print(obj.preço)