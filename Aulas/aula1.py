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
# nome = input("Digite seu nome: ")
# idade = int(input("Digite a sua idade: "))
# altura = float(input("Digite a sua altura: "))
# print(nome, idade, altura)

# print(hex(idade))
# print(bin(idade))
# print(oct(idade))

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
# 1) Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante incomoda"?
e = "Um elefante incomoda muita gente"
print(e[3:20])

# 2) Escreva um programa que solicite uma frase ao usuário e reescreva a frase toda em maiúscula e sem espaços em branco.
frase = input("Digite uma frase: ")
print(frase.upper().replace(" ", ""))

# 3) Escreva um programa que solicite uma frase ao usuário e reescreva a frase usando “leet speak”. Por exemplo, hello -> h3110, leet -> 1337, gaming -> g4m1ng, password -> p455w0rd. Utilize a função replace neste caso.

frase2 = input("Digite uma frase: ")
print(frase2.replace("", ""))