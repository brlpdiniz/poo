# Relógio em en-us

# Parte importada do (GPT - não necessária)
import time
def contar_segundos(tempo):
    for segundo in range(1, tempo + 1):
        print(segundo)
        time.sleep(1)

class Clock:
    def __init__(self, h=0, m=0, s=0, p=True):
        self.hora = h
        self.min = m
        self.seg = s
        self.is_pm = p

    def __str__(self):
        pm = 'pm' if self.is_pm == True else 'am'
        return f'{self.hora}:{self.min}:{self.seg} {pm}'
    
    def advance(self):
        self.seg +=1
        if self.seg == 60:
            self.seg = 0
            self.min += 1
        if self.min == 60:
            self.min = 0
            self.hora += 1
        if self.hora == 12:
            self.hora = 0
            self.is_pm = True if self.is_pm == False else False

#main
relogio1 = Clock()

class Calendar:
    def __init__(self, d=1, m=1, a=1900):
        self.dia = d
        self.mes = m
        self.ano = a
        self.__dias = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __str__(self):
        return f'{self.dia:02d}:{self.mes:02d}:{self.ano:04d}'

    def advance(self):
        self.dia += 1
        if self.dia > self.__dias[self.mes]:
            self.dia = 1
            self.mes += 1

        if self.mes == 13:
            self.mes == 1
            self.ano += 1
#main
cal1 = Calendar(29,12,2024)
for i in range(40):
    cal1.advance()
    print ( cal1 )


class ClockCalendar(Clock, Calendar):
    def __init__(self, h=0, mi=0, s=0, p=True, d=1, m=1, a=1900):
        Clock.__init__(self, h, mi, s, p)
        Calendar.__init__(self, d, m, a)
    
    def __str__(self):
        aux = Clock.__str__(self)
        aux += ' de '
        aux += Calendar.__str__(self)
        return aux

    def advance(self):
        Clock.advance(self)
        if self.hora== 0 and self.min == 0 and self.seg == 0 and self.is_pm == False:
            Calendar.advance(self)

#main
cc = ClockCalendar(11,58,34,True,31,1,2024)