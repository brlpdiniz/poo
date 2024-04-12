class Data:
    def __init__(self, d=0, m=0, a=0):
        self.dia = d
        self.mes = m
        self.ano = a

    def input(self):
        self.dia = int(input('Entre com o dia: '))
        self.mes = int(input('Entre com o mês: '))
        self.ano = int(input('Entre com o ano: '))

    def __str__(self):
        return f'{self.dia:02}/{self.mes:02}/{self.ano:04}'

class Pessoa:
    def __init__(self, c=0, n='', d=Data()):
        self.codigo = c
        self.nome = n
        self.dtNasc = d
    
    def input(self):
        print('Pessoa')
        self.nome = input('Entre com o nome: ')
        self.codigo = int(input('Entre com o código: '))
        print('Data Nascimento')
        self.dtNasc.input()

    def __str__(self):
        aux = 'PESSOA\n======\n'
        aux += f'nome.............> {self.nome}\n'
        aux += f'código...........> {self.codigo}\n'
        aux += f'data nascimento..> {self.dtNasc}'
        return aux

#main
d1 = Data()
d1.input()
print(d1)

d2 = Data(12,4,2024)
print(d2)

p1 = Pessoa(45)
print(p1)

p2 = Pessoa(34,'João Adalberto',Data(5,5,1955))
print(p2)