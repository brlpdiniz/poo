## Parte Prática
### 1 - Fazer uma classe Fração com:
    # * Adição de 2 racionais
    # * Subtração de 2 racionais
    # * Multiplicação de 2 racionais
    # * Inverter numerador e denominador
    # * Converter para float
    # * Calcular o complemento
    # * Minimizar o número (método privado)
    # - No main, fazer uma lista de frações e testar seus métodos.

class Fração:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def mostra(self):
        print(f'{self.num}/{self.den}')

    def adição(self, fração2):
        novo_numerador = (self.num * fração2.den) + (fração2.num * self.den)
        novo_denominador = self.den * fração2.den
        resultado = Fração(novo_numerador, novo_denominador)
        return resultado

    def subtração(self, fração2):
        novo_numerador = (self.num * fração2.den) - (fração2.num * self.den)
        novo_denominador = self.den * fração2.den
        resultado = Fração(novo_numerador, novo_denominador)
        return resultado


    def multiplicação(self, fração2):
        novo_numerador = self.num * fração2.num
        novo_denominador = self.num * fração2.den
        resultado = Fração(novo_numerador, novo_denominador)
        return resultado
    
    def inversor(self):
        novo_numerador = self.den
        novo_denominador = self.num
        resultado = Fração(novo_numerador, novo_denominador)
        return resultado

    def conversor(self):
        numerador_convertido = float(self.num)
        denominador_convertido = float(self.den)
        resultado = Fração(numerador_convertido, denominador_convertido)
        return resultado
    
    # Maximizar o número (método privado)
    def minimizar(self):
        mdc = self.__mdc(self.num, self.den)
        novo_numerador = self.num
        novo_denominador = self.den
        resultado = Fração(novo_numerador, novo_numerador)
        return resultado
    
    def __mdc(self, a, b):
        while b:
            a, b = b, a%b
            return a

#main
m = Fração(10,20)
m.mostra()

n = Fração(25,30)

resultado_adicao = m.adição(n)
resultado_adicao.mostra()

resultado_subtracao = m.subtração(n)
resultado_subtracao.mostra()

resultado_multiplicacao = m.multiplicação(n)
resultado_multiplicacao.mostra()

resultado_inversor = m.inversor()
resultado_inversor.mostra()

resultado_conversor = m.conversor()
resultado_conversor.mostra()

resultado_minimizar = m.minimizar()
resultado_minimizar.mostra()