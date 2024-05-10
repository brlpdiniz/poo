class Data:
    def __init__(self, dia = 1, mes = 1, ano = 1600):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    # isBissexto():bool
    def isBissexto(self) -> bool:
        if (self.ano % 4 == 0 and self.ano % 100 != 0 ) or (self.ano % 400 == 0):
            return True
        else:
            return False

    # trimestre():int
    def trimestre(self) -> int:
        
            return 
    
    # numDiasMes():int
    def numDiasMes(self) -> int:
        if (self.mes == 1 or 3 or 5 or 7 or 8 or 10 or 12):
            return
    
    #dataValida():bool
    def dataValida(self) -> bool:
        return
    
    # mostra():void
    def mostra(self):
        print()
        print()
        print()
        print()
        print()

# main