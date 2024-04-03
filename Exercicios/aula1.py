import math

a = 'Bruno'
b = "Bruno"
c = 25
d = True
print(a,b,c,d)

# 2.6 Exercícios: Variáveis
# 1) Escreva mais 3 identificadores que não possam ser usados como nome de variáveis.
    # $Variavel
    # @Variavel
    # 2Variavel3

# 2) Experimente as funções de conversão de base.
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
print(nome, idade, altura)

print(hex(idade))
print(bin(idade))
print(oct(idade))

# 3) Experimente também a forma de formatação de string para converter números entre diferentes bases.
x = 255
oct_string = f"{x} in oct is: {x:o}"
print(oct_string)
print(f"{x} in bin is: {x:b}")

print ("Hello World!")

print("Apostila " + "de Matematica")

a2 = "apostila"
b2 = " de Português"
c2 = a2+b2
print(c)

# Concatenar a mesma string múltiplas vezes
print(b2*5)

# Tamanho da string
print(len(c2))

# Primeira letra maiuscula
print(a2.capitalize())


# 3.4 Exercícios: Strings
# a) Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante incomoda"?
e = "Um elefante incomoda muita gente"
print(e[3:20])

# b) Escreva um programa que solicite uma frase ao usuário e reescreva a frase toda em maiúscula e sem espaços em branco.
frase = input("Digite uma frase: ")
print(frase.upper().replace(" ", ""))

# c) Escreva um programa que solicite uma frase ao usuário e reescreva a frase usando “leet speak”. Por exemplo, hello -> h3110, leet -> 1337, gaming -> g4m1ng, password -> p455w0rd. Utilize a função replace neste caso.

frase2 = (input("Digite uma frase: "))
frase2 = frase2.upper()
frase2.replace("a", "4")
frase2.replace("e", "3")
frase2.replace("i", "1")
frase2.replace("l", "1")
frase2.replace("o", "0")
frase2.replace("s", "5")

# 4.2 Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
#     (x² + y² )
# z = __________
#     ( x − y )²

w = int(input("Digite o valor de W: "))
z = int(input("Digite o valor de Z: "))

result = (w*w+z*z)/((w-z)**2)
print(result)


# 4.3) Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 35%.
salario = float(input("Digite o seu salário: "))
salario2 = salario * 1.35

print ("Parabéns, seu novo salário é: {salario2}")


# 4.4) Escreva um programa que ache as raízes da equação 2x2 – 18x + 12.
a = 2
b = -18
c = 12
delta = (b ** 2) -4*a*c

x1 = (-b) + math.sqrt(delta) / (2*a)
x2 = (-b) - math.sqrt(delta) / (2*a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")