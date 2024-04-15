# O código deve estar organizado em arquivos separados e comentado
# O jogo deve possuir um sistema de salvamento caso o jogador saia do jogo e deseje salvar (talvez - memorizadores)
# O jogo deve possuir um sistema de ranqueamento (hiscore) de acordo com o tamanho da palavra e a quantidade de erros por acertos. Ex: Uma palavra de 10 letras e o jogador acertou de primeira sem errar nenhuma, ele deve conseguir uma pontuação maior do que outros jogadores que tenham acertado uma palavra menor.
# Fazer o gerador de palavras aleatórias como um classe a parte

import random

# função do gerador de palavras aleatórias -> tem que ser classe
def selecionarPalavra():
    palavras = ['teste', 'abacate', 'abacaxi', 'banana', 'maça']
    return random.choice(palavras)

def cenarios_forca(vidasFaltantes):
    cenarios = [
        '''
         --------
         |      |
         |      O
         |     /|\\
         |      |
         |     / \\
         --------''',
         '''
         --------
         |      |
         |      O
         |     /|\\
         |      |
         |     /
         --------''',
         '''
         --------
         |      |
         |      O
         |     /|\\
         |      |
         |
         --------''',
         '''
         --------
         |      |
         |      O
         |      |/
         |      |
         |
         --------''', 
        '''
         --------
         |      |
         |      O
         |      |
         |      |
         |
         --------''',          
        '''
         --------
         |      |
         |      O
         |
         |
         |
         --------''',
         '''
         --------
         |      |
         |
         |
         |
         |
         --------''',
    ]
    return cenarios[vidasFaltantes]

def main():
    palavra = selecionarPalavra()
    letraChutada = []
    vidasFaltantes = 7
    palavraChutada = ['_'] * len(palavra)

    print('Bem vindo ao Jogo da Forca, vamos começar!')
    print('_' * len(palavra))
    print()

    while vidasFaltantes > 0 and '_' in palavraChutada:
        tentativa = input('Arrisque uma letra ou digite "sair: " ').lower()

        if tentativa == 'sair':
            print('Saindo do jogo!')
            break

        if tentativa in letraChutada:
            print('Esta letra já foi chutada, tente novamente!')
        else:
            letraChutada.append(tentativa)

            if tentativa in palavra:
                # guarda a palavra com um ID (de 0 até o final da palavra)
                for i, letra in enumerate(palavra):
                    if letra == tentativa:
                        palavraChutada[i] = letra
            else:
                vidasFaltantes -= 1
                print(cenarios_forca(vidasFaltantes))
                print('Faiô!')

        print(' '.join(palavraChutada))
        print()

    if '_' not in palavraChutada:
        print('Parabéns! Você acertou a palavra!')
    elif vidasFaltantes == 0:
        print('O seu boneco foi enforcado! A palavra era: ', palavra)

if __name__ == '__main__':
    main()