# Resumo - POO - 2º Bimestre

### Herança Simples (classe derivada)
- Processo de criação
    * de novas classes (classe derivada)
    * baseado em classes existentes (classe base)
- A classe derivada herda todas as características da
classe base, além de incluir características próprias
adicionais
- Reutilização de Código
- Própria classe -> Tudo
- Classes derivadas -> Público e Protegido!
- Outros -> Público

#### Ser X Ter
- Herança (SER)
    * Um Cliente é uma Pessoa.
    * Um Funcionário é uma Pessoa.
    * Uma Conta Corrente é uma Conta.
- Composição (TER)
    * Uma Pessoa tem uma Data de Aniversário.
    * Um Cliente tem uma senha.
    * Uma Conta tem um saldo.

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
    * Este módulo fornece a infraestrutura para definir classes base abstratas
```
from abc import ABC, abstractmethod
class Veículo(ABC):
    @abstractmethod
    def num_portas(self):
        pass
    def motor(self):
        print("Flex")
class Carro(Veículo):
    def num_portas(self):
        print("Quatro")
class Moto(Veículo):
    def num_portas(self):
        print("Zero")
carro1 = Carro()
carro1.motor()
carro1.num_portas()
```



### Herança Múltipla






### Interfaces






### Polimorfismo e outros






### Singleton




