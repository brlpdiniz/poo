# Classe Monitor

class Monitor1:
    def __init__(self, x, y):
        self.stLigado = False
        self.resolucaoX = x
        self.resolucaoY = y

#main
m = Monitor1(800, 600)

print(m.resolucaoX)
print(m.resolucaoY)


class Monitor3:
    def ligar(self):
        self.__stLigado = True
    
    def desligar(self):
        self.__stLigado = False

    def alterarResolução(self, x:int, y:int):
        self.resoluçãoX = x
        self.resoluçãoY = y
    
    def status(self) -> bool:
        return self.__stLigado

print(f"O status é: ", )


class Monitor4:
    def ligar(self):
        self.__stLigado = True
        self.__log('Ligando')
    
    def desligar(self):
        self.__stLigado = False
        self.__log('Desligando')
    
    def alterarResolução(self, x:int, y:int):
        self.resoluçãoX = x
        self.resoluçãoY = y
        self.__log('Alterando resolução')
    
    