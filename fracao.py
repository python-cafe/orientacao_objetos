# Autor: Hallison Paz
# Canal Python Café: https://youtube.com/pythoncafe
# Programação Orientada a Objetos em Python
# Vídeo: Classes | Orientação a Objetos #2


# Modelando uma fração
# Atributos
# 1. numerador; 2 denominador

# Métodos
# somar; subtrair; multiplicar; dividir; inverter; negar; simplificar

class Fracao:

    def __init__(self, num, den):
        self.numerador = num
        if den ==0:
            self.denominador = 1
        else:
            self.denominador = den

    def somar(self, outra):
        if self.denominador == outra.denominador:
            num = self.numerador + outra.numerador
            den = self.denominador
            return Fracao(num, den)
        num = self.numerador * outra.denominador + outra.numerador*self.denominador
        den = self.denominador*outra.denominador
        return Fracao(num, den)

    def subtrair(self, outra):
        return self.somar(outra.negar())

    def multiplicar(self, outra):
        numer = self.numerador * outra.numerador
        denom = self.denominador * outra.denominador
        return Fracao(numer, denom)

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())

    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def negar(self):
        return Fracao(-self.numerador, self.denominador)

    def simplificar(self):
        pass

# teste
if __name__ == '__main__':
    a = Fracao(4, 5)
    b = Fracao(-2, 7)

    resultado = a.multiplicar(b)
    # b = Fracao.inverter(a)
    c = a.inverter()
    # palavra = "ninja"
    # nova = palavra.upper()
