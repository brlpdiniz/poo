from abc import ABC, abstractmethod

class Aluguel(ABC):
    @abstractmethod
    def diarista(self, quilometragem: int):
        pass

    @abstractmethod
    def semanista(self, quilometragem: int):
        pass

    @abstractmethod
    def mensalista(self, quilometragem: int):
        pass

class Veiculo(ABC):
    def __init__(self, preco: float, ano: int):
        self.preco = preco
        self.ano = ano

    @abstractmethod
    def calcular_faixa_quilometragem(self, quilometragem: int):
        pass

class Moto(Veiculo, Aluguel):
    def calcular_faixa_quilometragem(self, quilometragem: int):
        # Calcula a faixa de quilometragem (FQ)
        if quilometragem <= 200:
            return 50  # Valor de exemplo para a faixa
        elif quilometragem <= 400:
            return 100
        elif quilometragem <= 1250:
            return 200
        elif quilometragem <= 1500:
            return 300
        else:
            return 500

    def diarista(self, quilometragem: int):
        fq = self.calcular_faixa_quilometragem(quilometragem)
        return 0.005 * self.preco + 500 + fq

    def semanista(self, quilometragem: int):
        valor_diaria = self.diarista(quilometragem)
        return 7 * valor_diaria * 0.9  # Desconto de 10%

    def mensalista(self, quilometragem: int):
        valor_semanal = self.semanista(quilometragem)
        return 4.5 * valor_semanal * 0.85  # Desconto de 15%

class CarroPasseio(Veiculo, Aluguel):
    def __init__(self, preco: float, ano: int, num_passageiros: int):
        super().__init__(preco, ano)
        self.num_passageiros = num_passageiros

    def calcular_faixa_quilometragem(self, quilometragem: int):
        if quilometragem <= 200:
            return 50
        elif quilometragem <= 400:
            return 100
        elif quilometragem <= 1250:
            return 200
        elif quilometragem <= 1500:
            return 300
        else:
            return 500

    def diarista(self, quilometragem: int):
        fq = self.calcular_faixa_quilometragem(quilometragem)
        return 0.002 * self.preco + fq

    def semanista(self, quilometragem: int):
        valor_diaria = self.diarista(quilometragem)
        return 7 * valor_diaria * 0.9  # Desconto de 10%

    def mensalista(self, quilometragem: int):
        valor_semanal = self.semanista(quilometragem)
        return 4.5 * valor_semanal * 0.85  # Desconto de 15%

class Caminhao(Veiculo, Aluguel):
    def __init__(self, preco: float, ano: int, peso_maximo_carga: float):
        super().__init__(preco, ano)
        self.peso_maximo_carga = peso_maximo_carga

    def calcular_faixa_quilometragem(self, quilometragem: int):
        if quilometragem <= 200:
            return 50
        elif quilometragem <= 400:
            return 100
        elif quilometragem <= 1250:
            return 200
        elif quilometragem <= 1500:
            return 300
        else:
            return 500

    def diarista(self, quilometragem: int):
        fq = self.calcular_faixa_quilometragem(quilometragem)
        return 0.0005 * self.preco + 0.02 * self.peso_maximo_carga + fq

    def semanista(self, quilometragem: int):
        valor_diaria = self.diarista(quilometragem)
        return 7 * valor_diaria * 0.9  # Desconto de 10%

    def mensalista(self, quilometragem: int):
        valor_semanal = self.semanista(quilometragem)
        return 4.5 * valor_semanal * 0.85  # Desconto de 15%

if __name__ == "__main__":
    moto = Moto(preco=10000, ano=2020)
    carro = CarroPasseio(preco=30000, ano=2018, num_passageiros=5)
    caminhao = Caminhao(preco=50000, ano=2015, peso_maximo_carga=10000)

    quilometragem = 150  # Exemplo de quilometragem

    print("Moto:")
    print(f"Diária: {moto.diarista(quilometragem)}")
    print(f"Semanal: {moto.semanista(quilometragem)}")
    print(f"Mensal: {moto.mensalista(quilometragem)}")

    print("\nCarro de Passeio:")
    print(f"Diária: {carro.diarista(quilometragem)}")
    print(f"Semanal: {carro.semanista(quilometragem)}")
    print(f"Mensal: {carro.mensalista(quilometragem)}")

    print("\nCaminhão:")
    print(f"Diária: {caminhao.diarista(quilometragem)}")
    print(f"Semanal: {caminhao.semanista(quilometragem)}")
    print(f"Mensal: {caminhao.mensalista(quilometragem)}")
