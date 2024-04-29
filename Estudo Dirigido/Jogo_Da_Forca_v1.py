# O código deve estar organizado em arquivos separados e comentado
# O jogo deve possuir um sistema de salvamento caso o jogador saia do jogo e deseje salvar (talvez - memorizadores)
# O jogo deve possuir um sistema de ranqueamento (hiscore) de acordo com o tamanho da palavra e a quantidade de erros por acertos. Ex: Uma palavra de 10 letras e o jogador acertou de primeira sem errar nenhuma, ele deve conseguir uma pontuação maior do que outros jogadores que tenham acertado uma palavra menor.
# Fazer o gerador de palavras aleatórias como um classe a parte

import random
import json

    # Classe - Escolhe palavras aleatórias
class GeraPalavras:
    def __init__(self, temas, palavras):
        self.temas = temas
        self.palavras = palavras
        self.inicializarTemas()
        
        # Criar Temas
        # Fazer alguma lógica aqui de importar arquivo ou gerar classes de temas
    
    def inicializarTemas(self):
        self.temas['Animal'] = ['cachorro', 'gato', 'pássaro', 'elefante', 'leão']
        self.temas['Comida'] = ['abacate', 'abacaxi', 'banana', 'maçã', 'uva']
        self.temas['Objeto'] = ['cadeira', 'mesa', 'computador', 'telefone', 'livro']
        return 

    def selecionarPalavra(self, tema=None):
        if tema is None:
            tema = random.choice(list(self.temas.keys()))
        return random.choice(self.temas[tema])

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

# Salvamento do jogo em json
def salvar_jogo(palavra, letraChutada, vidasFaltantes, palavraChutada):
    data = {
        'palavra': palavra,
        'letraChutada': letraChutada,
        'vidasFaltantes': vidasFaltantes,
        'palavraChutada': palavraChutada
    }
    with open('salvo.json', 'w') as file:
        json.dump(data, file)

def carregar_jogo():
    try:
        with open('salvo.json', 'r') as file:
            data = json.load(file)
            return data['palavra'], data['letraChutada'], data['vidasFaltantes'], data['palavraChutada']
    except FileNotFoundError:
        return None, None, None, None

class Ranking:
    def __init__(self):
        self.rank = {}

    def atualizar_ranking(self, nome_jogador, tamanho_palavra, acertos, erros):
        pontuacao = tamanho_palavra * (acertos - erros)
        if nome_jogador in self.rank:
            self.rank[nome_jogador] += pontuacao
        else:
            self.rank[nome_jogador] = pontuacao

    def exibir_ranking(self):
        ranking_ordenado = sorted(self.rank.items(), key=lambda x: x[1], reverse=True)
        print("\nRanking:")
        for i, (jogador, pontuacao) in enumerate(ranking_ordenado, start=1):
            print(f"{i}. {jogador}: {pontuacao} pontos")

# função "main"
def main():
    palavra, letraChutada, vidasFaltantes, palavraChutada = carregar_jogo()
    if palavra is None:
        palavra = GeraPalavras(None, None).selecionarPalavra()
        letraChutada = []
        vidasFaltantes = 7
        palavraChutada = ['_'] * len(palavra)

    print('Bem vindo ao Jogo da Forca, vamos começar! \n')
    print(' '.join(palavraChutada))
    print(cenarios_forca(vidasFaltantes))

    while vidasFaltantes > 0 and '_' in palavraChutada:
        tentativa = input('Arrisque uma letra ou digite "sair" -> \n').lower()

        if tentativa == 'salvar':
            salvar_jogo(palavra, letraChutada, vidasFaltantes, palavraChutada)
            print('Jogo salvo. Até logo!')
            break

        if tentativa in letraChutada:
            print('Esta letra já foi chutada, tente novamente! \n')
        else:
            letraChutada.append(tentativa)

            if tentativa in palavra:
                # Enumerate -> guarda a palavra com um ID (de 0 até o final da palavra)
                for i, letra in enumerate(palavra):
                    if letra == tentativa:
                        palavraChutada[i] = letra
            else:
                vidasFaltantes -= 1
                print(cenarios_forca(vidasFaltantes))
                print('Faiô, tente novamente!')

        print(' '.join(palavraChutada))
        print()

    if '_' not in palavraChutada:
        print('Parabéns! Você acertou a palavra!')

    elif vidasFaltantes == 0:
        print('O seu boneco foi enforcado! (X_X) ☜ (◉▂◉ )')
        print('╭( ✖_✖ )╮')
        print('A palavra era: ', palavra)

if __name__ == '__main__':
    main()