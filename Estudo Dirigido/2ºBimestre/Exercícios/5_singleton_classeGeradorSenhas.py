from queue import Queue
import threading
import time
import random

# Singleton para Gerador de Senhas
class GeradorSenhas:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(GeradorSenhas, cls).__new__(cls)
                    cls._instance._contador_an = 0
                    cls._instance._contador_ap = 0
        return cls._instance

    def gerar_senha(self, tipo):
        if tipo == 'AN':
            self._contador_an += 1
            return f"AN{self._contador_an}"
        elif tipo == 'AP':
            self._contador_ap += 1
            return f"AP{self._contador_ap}"
        else:
            raise ValueError("Tipo de senha inválido. Use 'AN' ou 'AP'.")

# Filas para Senhas
fila_normal = Queue()
fila_preferencial = Queue()

# Atendentes (Produtores)
class Atendente(threading.Thread):
    def __init__(self, nome, tipo_fila):
        super().__init__()
        self.nome = nome
        self.tipo_fila = tipo_fila
        self.gerador_senhas = GeradorSenhas()

    def run(self):
        for _ in range(100):
            senha = self.gerador_senhas.gerar_senha(self.tipo_fila)
            if self.tipo_fila == 'AN':
                fila_normal.put(senha)
            else:
                fila_preferencial.put(senha)
            print(f"{self.nome} gerou senha: {senha}")
            time.sleep(random.uniform(1, 3))  # Simula o tempo para gerar uma nova senha

# Caixas (Consumidores)
class Caixa(threading.Thread):
    def __init__(self, nome, atende_preferencial=False):
        super().__init__()
        self.nome = nome
        self.atende_preferencial = atende_preferencial
        self.iteracoes = 100

    def run(self):
        while self.iteracoes > 0:
            if self.atende_preferencial:
                if not fila_preferencial.empty():
                    senha = fila_preferencial.get()
                    self.iteracoes -= 1
                else:
                    time.sleep(1)
                    continue
            else:
                if fila_preferencial.qsize() > 4:
                    senha = fila_preferencial.get() if self.iteracoes % 2 == 0 else fila_normal.get()
                else:
                    senha = fila_normal.get()
                self.iteracoes -= 1

            print(f"{self.nome} está atendendo a senha: {senha}")
            time.sleep(random.uniform(1, 10))  # Simula o tempo para atendimento

# Inicializando o Sistema
if __name__ == "__main__":
    # Criando atendentes
    atendentes = [
        Atendente("Atendente 1", "AN"),
        Atendente("Atendente 2", "AP"),
        Atendente("Atendente 3", "AN")
    ]

    # Criando caixas
    caixas = [
        Caixa("Caixa 1", atende_preferencial=True),
        Caixa("Caixa 2"),
        Caixa("Caixa 3"),
        Caixa("Caixa 4")
    ]

    # Iniciando atendentes
    for atendente in atendentes:
        atendente.start()

    # Iniciando caixas
    for caixa in caixas:
        caixa.start()

    # Esperando todos os threads terminarem
    for atendente in atendentes:
        atendente.join()

    for caixa in caixas:
        caixa.join()

    print("Simulação concluída.")