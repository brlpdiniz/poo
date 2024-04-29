import random
import json
import unicodedata


class GeraPalavras:
    def __init__(self, temas=None, palavras=None):
        self.temas = temas or {}
        self.palavras = palavras or []
        self.inicializarTemas()

    def inicializarTemas(self):
        if not self.temas:
            self.temas['Animal'] = ['cachorro', 'gato', 'pássaro', 'elefante', 'leão']
            self.temas['Comida'] = ['abacate', 'abacaxi', 'banana', 'maçã', 'uva']
            self.temas['Objeto'] = ['cadeira', 'mesa', 'computador', 'telefone', 'livro']

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
    return cenarios[min(vidasFaltantes, len(cenarios) - 1)]

def remover_acentos(palavra):
    return ''.join(c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn')

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
            palavra = data.get('palavra', None)
            letraChutada = data.get('letraChutada', [])
            vidasFaltantes = data.get('vidasFaltantes', 7)
            palavraChutada = data.get('palavraChutada', ['_'] * len(palavra) if palavra else [])
            return palavra, letraChutada, vidasFaltantes, palavraChutada
    except FileNotFoundError:
        return None, None, None, None

class Ranking:
    def __init__(self):
        self.rank = {}

    def atualizar_ranking(self, nome_jogador, erros):
        valor = 100 - (erros / 7)
        if erros == 7:
            valor = 0
        
        pontuacao = valor

        if nome_jogador in self.rank:
            self.rank[nome_jogador] += pontuacao
        else:
            self.rank[nome_jogador] = pontuacao

    def exibir_ranking(self):
        ranking_ordenado = sorted(self.rank.items(), key=lambda x: x[1], reverse=True)
        print("\nRanking:")
        for i, (jogador, pontuacao) in enumerate(ranking_ordenado, start=1):
            print(f"{i}. {jogador}: {pontuacao} pontos")


def main():
    continuar_jogando = True
    ranking = Ranking()
    while continuar_jogando:
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

            if tentativa == 'sair':
                print('Saindo. Até logo!')
                continuar_jogando = False
                break

            if tentativa in letraChutada:
                print('Esta letra já foi chutada, tente novamente! \n')
            else:
                letra_normalizada = remover_acentos(tentativa)
                letraChutada.append(letra_normalizada)

                if letra_normalizada in remover_acentos(palavra):
                    for i, letra in enumerate(palavra):
                        if remover_acentos(letra) == letra_normalizada:
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

        if continuar_jogando:
            nome_jogador = input('Digite seu nome para salvar o ranking ou digite "sair" para encerrar: ')
            if nome_jogador == 'sair':
                continuar_jogando = False
                ranking.exibir_ranking()
            else:
                ranking.atualizar_ranking(nome_jogador, 7 - vidasFaltantes)

if __name__ == '__main__':
    main()
