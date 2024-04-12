class Somador:
    def __init__(self, v=0):
        self.valor = v
    
    def soma(self, v):
        self.valor += v
    
    def getValor(self):
        return self.valor
    
    def __str__(self):
        aux = f'Total: {self.soma.getValor()}'
        aux += f'\nQuantidade: {self.qtd.getValor()}'
        aux += f'\nMédia: {self.getMedia()}'
        return aux
    
class Media:
    def __init__(self):
        self.soma = Somador()
        self.qtd = Somador()
    
    def adiciona(self,v):
        self.soma.soma(v)
        self.qtd.soma(1)
    
    def getMedia(self):
        return self.soma.getValor() / self.qtd.getValor()
    
    def __str__(self):
        aux = f'Total: {self.soma.getValor()}'
        aux += f'\nQuantidade: {self.qtd.getValor()}'
        aux += f'\nMédia: {self.getMedia()}'
        return aux
    
#Main
m1 = Media()
valor = 0

while valor >= 0:
    valor = float(input("Digite um valor positivo (negativo encerra): "))
    if valor > 0:
        m1.adiciona(valor)

print(m1)