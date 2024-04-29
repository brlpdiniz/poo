## POO - Programação Orientada a Objetos - Estudo Dirigido
### Profº: Diógenes Cogo Furlan

# | GRR | NOME |
# | 2017208552 | Bruno Leandro Diniz |
# | 2023188925 | Gabriel Luiz Boch |

import random
import json
import unicodedata

# Classe responsável por gerar palavras aleatórias de diferentes temas
class GeraPalavras:
    def __init__(self, temas=None, palavras=None):
        self.temas = temas or {}
        self.palavras = palavras or []
        self.inicializarTemas(usuarioTema = 0)

    def inicializarTemas(self, usuarioTema):
        # Inicializa os temas com palavras
        self.temas['Animal'] = ['cachorro', 'gato', 'pássaro', 'elefante', 'leão', 'tigre', 'leopardo', 'zebra', 'girafa', 'rinoceronte', 'macaco', 'hipopótamo', 'crocodilo', 'lobo', 'coelho', 'panda', 'peixe', 'pombo', 'golfinho']
        self.temas['Comida'] = ['abacate', 'abacaxi', 'banana', 'maçã', 'uva', 'melancia', 'laranja', 'pera', 'melão', 'morango', 'pêssego', 'kiwi', 'amora', 'figo', 'caqui', 'pitaya', 'goiaba', 'jabuticaba', 'acerola', 'framboesa']
        self.temas['Objeto'] = ['cadeira', 'mesa', 'computador', 'telefone', 'livro', 'escova', 'vassoura', 'martelo', 'chave', 'tesoura', 'panela', 'caneca', 'abajur', 'espelho', 'copo', 'pente', 'relógio', 'máquina', 'teclado', 'mouse']

        print('\nBem vindo ao Jogo da Forca, vamos começar! \n')
        print('Animal = 1')
        print('Comida = 2')
        print('Objeto = 3')
        
        usuarioTema = input('\nEscolha o tema que gostaria de jogar (1, 2 ou 3): ')
        if usuarioTema == 1:
            self.temas = self.temas['Animal']
        elif usuarioTema == 2:
            self.temas = self.temas['Comida']
        elif usuarioTema == 3:
            self.temas = self.temas['Objeto']
        else:
            print('Insira uma opção de tema válida!')
            (parar o programa aqui)
            

    #  selecionar uma palavra aleatória de um tema específico
    def selecionarPalavra(self, tema=None):
        tema = random.choice(list(self.temas.keys()))
        return random.choice(self.temas[tema])

# Retorna os bonecos da forca
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

# função para remover os acentos
def remover_acentos(palavra):
    return ''.join(c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn')

# Função para salvar o estado do jogo em um arquivo JSON
def salvar_jogo(palavra, letraChutada, vidasFaltantes, palavraChutada):
    data = {
        'palavra': palavra,
        'letraChutada': letraChutada,
        'vidasFaltantes': vidasFaltantes,
        'palavraChutada': palavraChutada
    }
    with open('salvo.json', 'w') as file:
        json.dump(data, file)

# Carrega o estado do jogo do JSON
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
        self.rank = {}  # Dicionário de jogadores e suas pontuações

    # Atualiza o ranking com a pontuação
    def atualizar_ranking(self, nome_jogador, erros):
        valor = 100 - (erros / 7)
        if erros == 7:
            valor = 0

        pontuacao = valor

# Se o jogador já está no ranking, adiciona a pontuação
        if nome_jogador in self.rank:
            self.rank[nome_jogador] += pontuacao
        else:
            self.rank[nome_jogador] = pontuacao

# Exibe o ranking ordenado por pontuação
    def exibir_ranking(self):
        ranking_ordenado = sorted(self.rank.items(), key=lambda x: x[1], reverse=True)
        print("\nRanking:")
        for i, (jogador, pontuacao) in enumerate(ranking_ordenado, start=1):
            print(f"{i}. {jogador}: {pontuacao:.2f} pontos") 

def main():
    continuar_jogando = True
    ranking = Ranking()
    while continuar_jogando:
        palavra, letraChutada, vidasFaltantes, palavraChutada = carregar_jogo()
        #Se não houver jogo salvo, gera uma nova palavra e reseta o jogo
        if palavra is None:
            palavra = GeraPalavras(None, None).selecionarPalavra()
            letraChutada = []
            vidasFaltantes = 7
            palavraChutada = ['_'] * len(palavra)
        
        # Início do jogo
        print('Bem vindo ao Jogo da Forca, vamos começar! \n')
        print(' '.join(palavraChutada))
        print(cenarios_forca(vidasFaltantes))

        while vidasFaltantes > 0 and '_' in palavraChutada:
            tentativa = input('Arrisque uma letra ou digite "sair" -> \n').lower()

            # Se o jogador digitar 'sair', encerra o jogo
            if tentativa == 'sair':
                continuar_jogando = False
                ranking.exibir_ranking()
                print('Saindo. Até logo!')
                break

            if tentativa in letraChutada:
                print('Esta letra já foi chutada, tente novamente! \n')
            else:
                letra_normalizada = remover_acentos(tentativa)
                letraChutada.append(letra_normalizada)

                # Se a letra está na palavra, preenche a palavra
                if letra_normalizada in remover_acentos(palavra):
                    for i, letra in enumerate(palavra):
                        if remover_acentos(letra) == letra_normalizada:
                            palavraChutada[i] = letra
                # Se a letra não está na palavra, diminui as vidas e exibe o boneco da forca
                else:
                    vidasFaltantes -= 1
                    print(cenarios_forca(vidasFaltantes))
                    print('Faiô, tente novamente!')

            print(' '.join(palavraChutada))
            print()

        # Se todas as letras foram descobertas, o jogador ganha
        if '_' not in palavraChutada:
            print('Parabéns! Você acertou a palavra!')

        elif vidasFaltantes == 0:
            print('O seu boneco foi enforcado! (X_X) ☜ (◉▂◉ )')
            print('╭( ✖_✖ )╮')
            print('A palavra era: ', palavra)

        if continuar_jogando:
            nome_jogador = input('Digite seu nome para salvar o ranking ou digite "sair" para encerrar: ')
            if nome_jogador == 'sair': # Se o jogador digitar 'sair', encerra o jogo
                continuar_jogando = False
                ranking.exibir_ranking() # Exibe o ranking antes de sair
            else:
                # Se o jogador digitar um nome, atualiza o ranking com a pontuação do jogador
                ranking.atualizar_ranking(nome_jogador, 7 - vidasFaltantes)

# Verifica se o script está sendo executado diretamente e chama a função main()
if __name__ == '__main__':
    main()
