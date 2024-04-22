## Resumo Prova 1 - APOO - Análise e Projeto Orientada a Objeto
### Profª: Marcia Regina M Cassitas Hino

| GRR | NOME |
| ------ | ------ |
| 2017208552 | Bruno Leandro Diniz |

### Classe
- É um tipo definido pelo usuário que contém o molde, a especificação para os objetos (modelo)
    - Definir uma classe envolve trabalhar com atributos (dados) e funções (código)

### Objeto
- É uma instancia de uma classe
- Conceito idêntico ao de Variável
- Objetos podem modelar entidades do mundo real

### Atributo
- São as variáveis “locais” da classe
- Um atributo é chamado de propriedade quando:
    - é um atributo “privado”
    - possui métodos controladores “get” e “set”

### Metodo
- São as “rotinas” que utilizam aquela estrutura 
- Quando uma função membro é chamada, se diz que o objeto está recebendo uma mensagem (para executar uma ação).

### Exemplos de Classes
| Diagrama UML de Classe |
| ------ |
|NOME CLASSE|
|ATRIBUTOS|
|MÉTODOS|

| Pessoa |
| ------ |
|nome: string|
|idade: int|
|altura: float|
|-------------|
|dizer_ola()|
|cozinhar()|
|andar()|

```
class Pessoa ():
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} de altura')

    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um: {receita} ')

    def andar(self, distancia):
        print(f'Saí para andar. Volto quando completar {distancia} metros!')

#main
pessoa = Pessoa(nome='Zhongli', idade = 30, altura = 1.90)
pessoa.dizer_ola()
pessoa.cozinhar('Spaghetti')
pessoa.andar(500)
```

### Self x Init
- self: vai aparecer sempre como 1º parâmetro de métodos de classe
    - é uma referencia ao próprio objeto

- __init__: método chamado de Construtor
    - é chamado ao se instanciar objetos
    - é nele que “setamos” os atributos do objeto

- Classe Contador – Python
```
class Contador:
    def __init__(self):
        self.codigo = 0
    def incrementa(self):
        self.codigo += 1
    def valor(self):
        return self.codigo
```

### Encapsulamento
- Construtores
    - Construtor é chamado automaticamente quando um objeto é criado 
    - Tem as funções de:
        * inicializar os atributos da classe
        * realizar operações necessárias para preparar o objeto para uso
    - Não são obrigatórios
    - Podem ser vazios
```
class Monitor1:
    def __init__(self, x, y):
        self.stLigado = False
        self.resolucaoX = x
        self.resolucaoY = y
#main
m = Monitor1(800, 600)
```

- Destrutores
    - É um método especial em programação que é chamado automaticamente quando um objeto é destruído ou liberado da memória
    - Tem as funções de:
        * realizar limpeza
        * liberar recursos associados ao objeto
    - Python não possui suporte a destrutor
        * utiliza "garbage collector"

- Visibilidade
    - É a forma com que os elementos de uma classe (atributos e métodos) podem ser vistos e utilizados externamente
    - Privado (-)
        * somente no interior da classe
        * Métodos e Atributos são declarados iniciando com 2 underlines (__)
        ```
        def ligar(self):
            self.__stLigado = true
            self.__log('Ligando')
        def __log(self, msg)
        ```

    - Protegido (#)
        * somente no interior da classe, e de suas herdeiras
    - Público (+)
        * dentro e fora da classe, de forma livre

- Programe a classe Fração
- Fração
- num: int
- den: int
+ Fração(num:int, den:int)
+ soma(Fração,Fração)
+ mostra()
+ toReal() : double









## Exercícios:
1) Defina até 5 atributos e 5 métodos para cada uma das seguintes classes (mostre também seu Diagrama UML):
– Carro
– Computador
– Conta
– Maçã
– Cliente
– Funcionário
― Data
― Casa
― Retângulo
― TV

2) Programe a classe Caixa:

| Caixa |
| ------ |
|altura: double|
|largura: double|
|profundidade: double|
|peso: double|
|empilhamento: int|
| ------ |
|area(): double|
|volume(): double|
|numCaixasSala( alt_sala, larg_sala, prof_sala ): int|

3) Programe uma das classes que você criou.
