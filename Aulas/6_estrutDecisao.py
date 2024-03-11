# 6.4 Estrutura de decisão
# 1) Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado
# (para ser aprovado a média deve ser no mínimo 6)

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
media = (nota1 + nota2)/2

if media >= 6:
    print(f"Aprovado! Sua média é {media}")
else:
    print(f"Reprovado! Sua média é {media}")

# 2) Refaça o exercício 1, identificando o conceito aprovado (média superior a 6), exame (média entre 4 e 6) ou reprovado (média inferior a 4). 

# 3) Dados 3 valores A, B, C verificar se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verificar se o triângulo é equilátero, isósceles ou escaleno. Para um polígono ser um triângulo, o comprimento de cada um de seus três lados deve ser menor do que a soma dos outros dois. 15
# A seguir, classifique-o:
#  Equilátero – 3 lados iguais
#  Isósceles – 2 lados iguais
#  Escaleno – 3 lados diferentes
    
# 4) Escreva um programa que recebe o peso e a altura de uma pessoa, e calcula seu IMC pela formula peso / (altura)² , e mostre o resultado baseado nas seguintes informações:
#  IMC abaixo de 20 – peso leve
#  entre 20 e 25 – peso normal
#  entre 25 e 30 – excesso de peso
#  entre 30 e 35 – obesidade leve
#  entre 35 e 40 – obesidade moderada
#  acima de 40 – obesidade mórbida

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura**2)

if (imc < 20):
    print("Peso Leve")
elif (imc >= 20 and imc < 25):
    print("Peso Normal")
elif (imc >= 25 and imc < 30):
    print("Excesso de Peso")
elif (imc >= 30 and imc < 35):
    print("Obesidade Leve")
elif (imc >= 35 and imc < 40):
    print("Obesidade Moderada")
else:
    print("Obesidade Mórbida")
    