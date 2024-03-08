# 5. ELista é um conjunto sequencial de valores, onde cada valor é identificado através de um índice. O primeiro valor tem índice 0. 
# Uma lista em Python é declarada da seguinte forma:
# Nome_Lista = [ valor1, valor2, ..., valorN]

# 5.6 Exercícios: listas
# 1) Dada a lista, escreva um programa que imprima as seguintes informações:
L = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista.
lêValor = len(L)
print(f"O tamanho da lista é: {lêValor}")

# b) maior valor da lista.
lêValor = max(L)
print(f"O valor máximo da lista é: {lêValor}")

# c) menor valor da lista.
lêValor = min(L)
print(f"O valor máximo da lista é: {lêValor}")

# d) soma de todos os elementos da lista.
lêValor = sum(L)
print(f"A soma dos elementos é: {lêValor}")

# e) lista em ordem crescente.
lêValor = L.sort()
print(f"A lista em ordem crescente fica: {lêValor}")

# f) lista em ordem decrescente.
lêValor = L.reverse()
print(f"A lista em ordem decrescente fica: {lêValor}")

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