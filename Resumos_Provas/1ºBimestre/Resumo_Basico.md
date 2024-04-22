## Resumo Prova 1 - APOO - Análise e Projeto Orientada a Objeto
### Profª: Marcia Regina M Cassitas Hino

| GRR | NOME |
| ------ | ------ |
| 2017208552 | Bruno Leandro Diniz |

### Variáveis
- Variáveis são pequenos espaços de memória, utilizados para armazenar e manipular dados. Os tipos de dados básicos são: int, float e string.
- Cada variável pode armazenar apenas um tipo de dado a cada instante.
- Não é preciso declarar de que tipo será cada variável no início do programa. Quando se faz uma atribuição de valor, automaticamente a variável se torna daquele tipo

#### Variáveis Globais
```
def soma(x,y):
    global total = x + y
```

### Comandos:
- Entrada de dados: input()

    `nome = input('Entre com seu nome: )`
- Saída de dados: print()

### Funções de conversão de base

`hex(x)`
`bin(x)`
`oct(x)`

### Identificadores
- Nomes de variáveis não podem começar com números
- Nomes de variáveis não podem conter espaços em branco
- Identificadores contendo caracteres especiais, como "@", "$", "#", etc

### Strings
- String é uma sequência de caracteres simples

    `print('Olá')`

- Para concatenar strings:

    `print('Apostila'+'Python')`

- Para se concatenar a mesma string múltiplas vezes:

    `print(var*5)`

- Funções (métodos) para manipular strings:

    `len()`
    `count`
    `isupper`

### Numbers
- int, long, float e complex

### Listas
- É um conjunto sequencial de valores, onde cada valor é identificado através de um índice. O primeiro valor tem índice 0.

    `L1 = [1, 2, 3, 4]`
    `print(L1[2])  -> 3`

- Uma lista pode ter valores de qualquer tipo, incluindo outras listas.

    `L2 = [1, 'abacate', 9.7, [3,5,7], 'Python']`

- Para alterar um elemento da lista, basta fazer uma atribuição de valor através do índice. O valor existente será substituído pelo novo valor.

    `L2[3] = 'morango'`

- Exemplos para manipular listas:

`len(), min(), max(), sum(), append(), extend(), sort(), reverse()`

- Transforma a string em uma lista, utilizando os espaços como referência:

```
m = "cana de açúcar"
m.split()
['cana', 'de', 'açúcar']
```

### Range
- range(n) : gera um intervalo de 0 a n-1
- range(i , n) : gera um intervalo de i a n-1
- range(i , n, p) : gera um intervalo de i a n-1 com intervalo p entre os números

### if - else
```
valor = int(input('Digite a sua idade: '))`
if valor < 18:
    print('Menor de idade')
elif valor >= 18 and valor < 65:
    print('Maior de idade')
else:
    print('Idoso')
```

### while
```
senha = '54321'
leitura = ''
while (leitura != senha):
    leitura = input("Digite a senha: ")
    if leitura == senha:
        print("Acesso liberado!")
    else:
        print("Senha incorreta. Tente novamente!)
        
-------------------------------------------------

- calcular 5 valores:
cont = 0, soma = 0
while cont < 5:
    cont = cont + 1
    valor = float(input('Digite o '+str(cont)+'-ésimo valor: '))
    soma = soma + valor
```

### for
```
for <variável> in range (início, limite, passo):
    <comandos>

for <variável> in <lista> :
    <comandos>

-------------------------------------------------
lista_notas = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
soma = 0
for nota in lista_notas:
    soma += nota
media = soma / len(lista_notas)
```


### Funções
```
def <nome_função> (<definição dos parâmetros >) :
    <Bloco de comandos da função>

def maior(x, y):
    if x > y:
        print(x)
    else:
        print(y)

maior(5,7)
```

### Return
- O comando return é usado para retornar um valor de uma função e encerrá-la. Caso não seja declarado um valor de retorno, a função retorna o valor **None**



## Exercícios:
1) Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante incomoda"?

2) Escreva um programa que solicite uma frase ao usuário e reescreva a frase toda em maiúscula e sem espaços em branco.

3) Escreva um programa que solicite uma frase ao usuário e reescreva a frase usando “leet speak”. Por exemplo, hello -> h3110, leet -> 1337, gaming -> g4m1ng, password -> p455w0rd. Utilize a função replace neste caso.

4) Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o
valor de z:
    z = ((x**2) + (y**2)) / ((x-y)**2)

5) Escreva um programa que receba o salário de um funcionário (float), e
retorne o resultado do novo salário com reajuste de 35%.

6) Escreva um programa que ache as raízes da equação 2x2 – 18x + 12.

7) Dada a lista L = [5, 7, 2, 9, 4, 1, 3] escreva um programa que imprima as seguintes informações:
- tamanho da lista.
- maior valor da lista.
- menor valor da lista.
- soma de todos os elementos da lista.
- lista em ordem crescente.
- lista em ordem decrescente.

8) Gere uma lista de contendo os múltiplos de 3 entre 1 e 50.

9) Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6)

10) Refaça o exercício 1, identificando o conceito aprovado (média superior a 6), exame (média entre 4 e 6) ou reprovado (média inferior a 4).

11) Dados 3 valores A, B, C verificar se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verificar se o triângulo é equilátero, isósceles ou escaleno. Para um polígono ser um triângulo, o comprimento de cada um de seus
três lados deve ser menor do que a soma dos outros dois.
- A seguir, classifique-o:
    * Equilátero – 3 lados iguais
    * Isósceles – 2 lados iguais
    * Escaleno – 3 lados diferentes

12) Escreva um programa que recebe o peso e a altura de uma pessoa, e calcula seu IMC pela formula peso / (altura)2 , e mostre o resultado baseado nas seguintes informações:
    * IMC abaixo de 20 – peso leve
    * entre 20 e 25 – peso normal
    * entre 25 e 30 – excesso de peso
    * entre 30 e 35 – obesidade leve
    * entre 35 e 40 – obesidade moderada
    * acima de 40 – obesidade mórbida

13) Escreva um programa para encontrar a soma S = 3 + 6 + 9 + …. + 333.

14) Escreva um programa que leia 10 notas e informe a média dos alunos.

15) Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.

16) Escreva um programa em Python que conte o número de vogais em uma string fornecida pelo usuário. O programa deve solicitar ao usuário que insira uma string e, em seguida, conte quantas vogais (as letras 'a', 'e', 'i', 'o', 'u' em minúsculas ou maiúsculas) estão presentes na string. Conte separadamente e também apresente o valor total (a soma de todas elas).

17) Crie uma função para desenhar uma linha, usando o caractere '_'. O tamanho da linha deve ser definido na chamada da função.

18) Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os.

19) Crie uma função que receba como parâmetro uma lista com valores
numéricos e retorne a média desses valores.

