# Revisão 2º Bimestre
- Classes são abstrações de elementos do mundo real. Os dados de uma classe não podem e não devem ser manipulados diretamente por uma funcionalidade implementada em outra classe. Na implementação de uma classe, qualquer alteração nos dados de uma classe deve acontecer pela invocação de um método da própria classe. Esta proteção é conhecida como -> Encapsulamento
- É correto afirmar que "um objeto da subclasse é, também, um objeto da superclasse, ou seja, os objetos da subclasse podem ser tratados como objetos da superclasse" -> Herança
- Em POO (Programação Orientada a Objetos), dizer que a classe A estende a classe B é o mesmo que dizer que -> A classe A é derivada de B;
- Os acessos e alterações dos dados de um objeto acontecem por meio de métodos implementados nesse objeto, para evitar que ocorram acessos diretos aos dados e assim evitando erros de alterações. Os dados ficam escondidos para dentro do objeto -> Encapsulamento
- Os objetos de uma classe podem herdar atributos e métodos de mais de uma classe base. Pode introduzir complexidade, como o problema do diamante de herança e ambiguidades -> Herança Múltipla
- É a característica única que permite que diferentes objetos respondam a mesma mensagem cada um a sua maneira. Em termos de programação, representa a capacidade de uma única referência invocar métodos diferentes, dependendo do seu conteúdo -> Polimorfismo
- Sejam A e B duas classes em um programa orientado a objetos. Se A é SUBCLASSE de B, então objetos da classe A PODEM POSSUIR MAIS atributos que objetos da classe B
- Neste exemplo, a classe Camisa está fazendo uma sobrescrita de método (são métodos diferentes)
I. a classe Camisa implementa um outro método cor, diferente daquele da classe Blusa.
IV. a classe Camisa poderá fazer uso de métodos pela herança direta da classeBlusa.
- De acordo com o código analisado, considere as seguintes asserções:
    - II. na linha 18 a classe B está herdando as características da classe base A;
    - III. a linha 26 contém polimorfismo (Sobrecarga).
- Verifique o código a seguir e selecione quais conceitos de OO estão sendo utilizados:
    - I. polimorfismo e herança.

#### Herança Simples (classe derivada)
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

#### Operadores
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

#### Atributos de Classes
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

#### Classe Abstrata
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

#### Herança Múltipla
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

#### Interfaces
- É um tipo de herança “fraca” -> é uma classe abstrata que contém SOMENTE métodos abstratos
- São as assinaturas do métodos {enviar(), receber(), fazer()}
- Somente é permitida a especificação de:
    * Constantes públicas e Métodos públicos e abstratos
- São proibidos:
    * Atributos e Métodos privados e protegidos
- Definem um comportamento -> Praticamente um “decorador”
```
class Cobrador(ABC):
    @abstractmethod
    def cobrarTaxa(self):
        pass
class ContaCorrente(Conta)
    def cobrarTaxa(self):
        self._saldo -= 10.0
```

#### Polimorfismo e outros
- O polimorfismo permite que diferentes classes tenham métodos com o mesmo nome, mas comportamentos diferentes.
- Em Python, isso pode ser facilmente implementado usando herança e sobrescrita de métodos.
- Existe 4 tipos:
    * Inclusão: um ponteiro da classe mãe pode apontar para uma instância de uma classe filha
    * Paramétrico: se restringe ao uso de templates (C++, por exemplo) e generics (C#/Java)
    * Sobrecarga: duas funções/métodos com o mesmo nome mas assinaturas diferentes
    * Coerção: conversão implícita de tipos sobre os parâmetros de uma função
- isinstance(): verifica se o objeto é uma instância de Type ou de qualquer subclasse de Tipo.
    * if isinstance(obj, str): print('obj é uma string ou subclasse de string')
- type(): verificar se o tipo de um objeto é exatamente tipo, excluindo quaisquer subclasses.
    * if type(objeto) is str: print('obj é exatamente uma string')
- x=100 y=90 -> print(x==y) #false -> print(x is y) #false
- a=[2],b=[2] -> print(a==b) #true -> print(x is y) #false
```
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass
class Cachorro(Animal):
    def fazer_som(self):
        return 'au au'
class Gato(Animal):
    def fazer_som(self):
        return 'miau'
animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.fazer_som())
```

#### Singleton
- Singleton é um dos padrões de criação que garante que:
    * uma classe tenha apenas uma instância;
    * e fornece um ponto de acesso global a essa instância.
- Como tornar uma classe Singleton?
    * 1. A classe vai conter o único objeto existente.
    * 2. Deve-se restringir o acesso ao construtor, tornando-o um construtor privado, de forma que novos objetos não possam ser criados.
    * 3. Então utilizar um método público que faça o controle da instanciação, de modo que ela só possa ser feita uma vez.
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