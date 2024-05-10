# Faça uma classe Playlist, que contenha uma lista de nomes de músicas
#    Para que a classe funcione "como uma lista", redefina os métodos:
#       __getitem__
#       __setitem__
#       __delitem__
#       __len__

class Playlist:
    def __init__(self):
        self.music = []
    
    def __getitem__(self, index):
        return self.music[index]

    def __setitem__(self, music, index):
        self.music[index] = music

    def __delitem__(self, index):
        self.music.remove(self.music[index])
    
    def __len__(self):
        return len(self.music)
        
    def adicionar_musica(self, music):
        self.music.append(music)

#main
play1 = Playlist()
play1.music.append('musica 1')
play1.music.append('musica 2')
play1.music.append('musica 3')

play1.music[1] = 'MUSICA 2'
print(play1)

for i in range(len(play1.music)):
    print(play1.music[i])