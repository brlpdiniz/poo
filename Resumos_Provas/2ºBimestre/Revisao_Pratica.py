from abc import ABC, abstractmethod

class PlacaDeVideo(ABC):
    def __init__(self, marca, modelo, memoria, clock):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.clock = clock
    def __str__(self):
        aux = 'f\nMarca:{self.marca}'
        aux += '\nModelo: {self.modelo}'
        aux += '\nMemoria: {self.memoria}'
        aux += '\nClock: {self.clock}'
        return aux
    @abstractmethod
    def calcular_perf(self):
        pass
    
class PlacaDeJogos(PlacaDeVideo):
    def __init__(self, marca, modelo, memoria, clock, suporte: bool):
        PlacaDeVideo.__init__(marca,modelo,memoria,clock)
        self.suporte = suporte
    def __str__(self):
        return PlacaDeVideo.__str__() + '\Suporte Ray Tracing: ' + self.suporte
    def calcular_perf(self):
        return self.clock * self.memoria

class PlacaProfissional(PlacaDeVideo):
    def __init__(self, marca: str, modelo: str, qtd_memoria: int, clock: float, certificacoes_software: list):
        super().__init__(marca, modelo, qtd_memoria, clock)
        self.certificacoes_software = certificacoes_software
    def __str__(self):
        return super().__str__() + f'Certificações de Software: {self.certificacoes_software}'
    def calcular_performance(self):
        return self.qtd_memoria * self.clock
    
class ColecoesDePlacaDeVideo:
    def __init__(self):
        self.lista_placas = []
    def adicionar_placa(self, placa: PlacaDeVideo):
        self.lista_placas.append(placa)
    def mostrar_melhor_performance(self):
        if not self.lista_placas:
            print("Nenhuma placa na coleção.")
            return
        melhor_placa = self.lista_placas[0]
        for placa in self.lista_placas:
            if placa.calcular_performance() > melhor_placa.calcular_performance():
                melhor_placa = placa
        print(f'Modelo com melhor performance: {melhor_placa.modelo}')
        melhor_placa.informacao()
#main
placa1 = PlacaDeJogos('NVIDIA', 'RTX 3080', 10, 1.71, True)
placa2 = PlacaProfissional('AMD', 'Radeon Pro WX 9100', 16, 1.25, ['Certificação A', 'Certificação B'])
colecao = ColecoesDePlacaDeVideo()
colecao.adicionar_placa(placa1)
colecao.adicionar_placa(placa2)
colecao.mostrar_melhor_performance()