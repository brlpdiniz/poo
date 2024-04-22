# Fazer uma classe Ponto3D com 3 atributos
#     - X
#     - Y
#     - Z
# * Os 3 atributos devem ser implementados como propriedades.
# * Fazer um método print() para mostrar o ponto inserido.

class Ponto3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z
    
    @z.setter
    def z(self, value):
        self.__z = value

    def mostra(self):
        print(f'Ponto x, y, z: ({self.__x}, {self.__y}, {self.__z})')

#main
m = Ponto3D(5,10,15)
m.mostra()