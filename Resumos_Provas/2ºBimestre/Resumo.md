# Resumo - POO - 2º Bimestre

### Herança Simples (classe derivada)
- Processo de criação
    * de novas classes (classe derivada)
    * baseado em classes existentes (classe base)
- A classe derivada herda todas as características da classe base, além de incluir características próprias adicionais
- Própria classe -> Tudo; - Classes derivadas -> Público e Protegido!

#### Ser X Ter
- Herança (SER)
    * Um Cliente é uma Pessoa; Um Funcionário é uma Pessoa; Uma Conta Corrente é uma Conta
- Composição (TER)
    * Uma Pessoa tem uma Data de Aniversário; Um Cliente tem uma senha; Uma Conta tem um saldo

#### Classe Pessoa e Classe Funcionário
```
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def __str__(self):
        return f'{self.nome} : {self.idade} anos'

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    def getSalarioAnual(self):
        return self.salario * 12
    
    def __str__(self):
        return super().__str__() + '\nSalário=' + str(self.salario)
    
    def getBonificação(self):
        return self.salario * 0.10
    
class Professor(Funcionario):
    def getBonificação(self):
        return self.salario * 0.15

class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def __str__(self):
        return super().__str__()

#main
f1 = Funcionario('Josias', 26, 3000)
p1 = Professor('Malaquias', 56, 5000)
a1 = Aluno('Bruno', 26)

print( f1.getBonificação() )
print( p1.getBonificação() )
print( a1.__str__())
```

#### Sobrescrita
- As subclasses podem ter métodos com o mesmo NOME que a classe pai (sobrecarga)
- As subclasses podem ter métodos com a mesma ASSINATURA que a classe pai (sobrescrita)
- Finalidades: Reescrita e Extensão

### Operadores
- Operadores podem ser sobrecarregados em classes através de métodos especiais conhecidos como métodos mágicos ou métodos especiais.
    * iniciam e terminam por __(2 underlines)

- __len__(self)
- __add__(self, other) - __sub__(self, other) - __mul__(self, other) - __truediv__(self, other) - Div Inteira __floordiv__(self, other) - Resto da Div __mod__(self, other) - __pow__(self, other) - __and__(self, other) - __or__(self, other)
- Adição: __pos__(self)
    * Este método é chamado quando um objeto é precedido por um sinal de adição (+).
- Subtração: __neg__(self)
    * Este método é chamado quando um objeto é precedido por um sinal de subtração (-).
- Absoluto: __abs__(self)
- Negação lógica: __not__(self) 
- Igualdade: __eq__(self, other)
- Diferença: __ne__(self, other)
- Menor que: __lt__(self, other)
- Menor ou igual a: __le__(self, other)
- Maior que: __gt__(self, other)
- Maior ou igual a: __ge__(self, other)
- Conversão para String: __str__(self)
- Conversão para Inteiro: __int__(self)
- Conversão para Float: __float__(self)
- Conversão para Booleano: __bool__(self)
- Acesso por Índice: __getitem__(self, key)
- Definição por Índice: __setitem__(self,key,value)
- Deleção por Índice: __delitem__(self, key)
- Comprimento (len): __len__(self)
- Iteração (iter): __iter__(self)
```
class Numero:
    def __init__(self, valor):
        self.valor = valor
    def __pos__(self):
        return +self.valor
    def __neg__(self):
        return -self.valor
    def __abs__(self):
        return abs(self.valor)
num1 = Numero(-5)
print("Pos=", +num1)
print("Pos=", -num1)
print("Abs=", abs(num1))

class Playlist:
    def __init__(self):
        self.musics = []
    def __getitem__(self,index):
        return self.musics[index]
    def __setitem__(self, index, music):
        self.musics[index] = music
    def __len__(self):
        return len(self.musics)
    def adicionar_musica(self, music):
        self.musics.append(music)
playlist = Playlist()
playlist.adicionar_music("Thriller)
print("Músicas na playlist:")
for musica in playlist:
    print('-', musica)

print("Músicas na playlist:")
for i in range(len(playlist)):
    print('-', playlist[i])
```

### Atributos de Classes
#### Atributo de classe é aquele que é compartilhado por todos os objetos pertencentes àquela classe (Variável ÚNICA dentro da classe)
#### Método de classe é um método que se comporta como uma função regular, mas pertence a uma classe.
    * recebe a classe como o primeiro argumento.
    * consegue manipular atributos da classe
    * o método não tem acesso à instância (self) na qual é chamado.
```
class Bebida:
    nome = "Bebida"   # atributo de classe
    @classmethod
    def imprimir_nome(cls):
        printn(f"Esta bebida é do tipo {cls.nome})

class Café(Bebida):
    nome = "Café"
class Chá(Bebida):
    nome = "Chá"
#main
Bebida.imprimir_nome()
Café.imprimir_nome()
Chá.imprimir_nome()
```

#### Método estático é um método que se comporta como uma função regular, mas pertence a uma classe.
- o método não tem acesso nem à classe (cls)
- o método não tem acesso à instância (self) na qual é chamado.
- não pode modificar o estado da instância do objeto nem o estado da classe.
```
class Classe1:
    def metodo_objeto(self):
        return 'met instancia chamado'
    @classmethod
    def metodo_classe(cls):
        return 'met classe chamado'
    @staticmethod
    def metodo_estatico():
        return 'met estatico chamado'
obj1 = Classe1()
print( obj1.metodo_objeto())
print( Classe1.metodo_classe())
print( Classe1.metodo_estatico())
```

### Classe Abstrata
- Classe Abstrata
    * Não pode ser instanciada
    * Só pode servir para herança
- Método Abstrato
    * Sem implementação
- Classe Final
    * Não pode ser herdada por outra classe
    * Obrigatoriamente folha
- Método Final
    * Não pode ser sobrescrito pelas suas subclasses
    * Obrigatoriamente herdado
- abc – abstract base class
```

from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def diametro(self):
        pass
    def __str__(self):
        aux = f"Area: {self.area()}"
        aux += f"\nPerimetro: {self.perimetro()}"
        aux += f"\nDiametro: {self.diametro()}"
        return aux

class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return self.lado * 4
    def diametro(self):
        return self.lado * math.sqrt(2)
q1 = Quadrado(5)
print(q1)

class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return (self.raio ** 2) * 3.14
    def perimetro(self):
        return self.raio * 2 * 3.14
    def diametro(self):
        return self.raio * 2
C1 = Circulo(5)
print(C1)

class Retangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
    def diametro(self):
        return math.sqrt(self.base**2 + self.altura**2)
R1 = Retangulo(5,8)
print(R1)

class Triangulo(Poligono):
    def __init__(self, base):
        self.base = base
    @abstractmethod
    def altura(self):
        pass
    def area(self):
        return (self.base * self.altura()) / 2
    def __str__(self):
        return super().__str__()

class TrianguloRetangulo(Triangulo):
    def __init__(self, cateto1, cateto2):
        super().__init__(base=cateto1)
        self.cateto1 = cateto1
        self.cateto2 = cateto2
    def altura(self):
        return self.cateto2
    def perimetro(self):
        return self.cateto1 + self.cateto2 + self.hipotenusa()
    def diametro(self):
        return self.hipotenusa()
    def hipotenusa(self):
        return math.sqrt(self.cateto1**2 + self.cateto2**2)
    def __str__(self):
        return super().__str__()
t1 = TrianguloRetangulo(3, 4)
print(t1)
```

### Herança Múltipla
- Um objeto pode conter “MUITOS” outros por composição; Um objeto quer ser “muitos” outros
- Algorítmo Diamante - ordem de resolução de
métodos
```
class Terreste(object):
    def __init__(self, velocidade=100):
        self.se_move_em_terra = True
        self.velocidade_em_terra = velocidade
    def __str__(self):
        aux = '\nse_move_em_terra = '
        aux += str(self.se_move_em_terra)
        aux += '\nvelocidade_em_terra = '
        aux += str(self.velocidade_em_terra)
        return aux
class Aquatico(object):
    def __init__(self, velocidade=5):
        self.se_move_na_agua = True
        self.velocidade_agua = velocidade
    def __str__(self):
        aux = '\nse_move_na_água = '
        aux += str(self.se_move_na_agua)
        aux += '\nvelocidade_agua = '
        aux += str(self.velocidade_agua)
        return aux
class Carro(Terreste):
    def __init__(self, veloc=120, pistoes=4):
        self.rodas = 4
        self.pistoes = pistoes
        Terreste.__init__(self, veloc)
    def __str__(self):
        aux = '\nrodas = ' + str(self.rodas)
        aux += '\npistões = ' + str(self.pistoes)
        aux += super().__str__()
        return aux
class Barco(Aquatico):
    def __init__(self, veloc=6, helices=1):
        self.helices = helices
        Aquatico.__init__(self, veloc)
    def __str__(self):
        aux = '\nhélices = ' + str(self.helices)
        aux += super().__str__()
        return aux
class Anfibio(Carro, Barco):
    def __init__(self, vt=80, va=4, pi=6, he=2):
        Carro.__init__(self, veloc=vt, pistoes=pi)
        Barco.__init__(self, veloc=va, helices=he)   
    def __str__(self):
        aux = Carro.__str__(self)
        aux += Barco.__str__(self)
        return aux
anf1 = Anfibio()
print(anf1)
```

### Interfaces
- É um tipo de herança “fraca”.
- Somente é permitida a especificação de:
    * Constantes públicas e Métodos públicos e abstratos
- São proibidos:
    * Atributos e Métodos privados e protegidos
- Definem um comportamento -> Praticamente um “decorador”





### Polimorfismo e outros




```
class Funcionario:
    def trabalhar(self):
    pass
class Gerente(Funcionario):
    def trabalhar(self):
    return "Gerente está gerenciando"
class Estagiario(Funcionario):
    def trabalhar(self):
    return "Estagiario está aprendendo"
def fazer_trabalho(funcionario):
    print(funcionario.trabalhar())
# Testando as classes
g = Gerente(); e = Estagiario()
fazer_trabalho(g); fazer_trabalho(e)
```

### Singleton




```
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
# main -> s1 = Singleton(); s2 = Singleton()
print(s1 is s2) # True
```