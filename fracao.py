# Autor: Hallison Paz
# Canal Python Café: https://youtube.com/pythoncafe
# Programação Orientada a Objetos em Python
# Vídeos: Classes | Orientação a Objetos #2
#         Representando Objetos em Strings | Orientação a Objetos #3


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

    # Representando Objetos em Strings | https://youtu.be/g9wIo-hBcgA
    def __str__(self):
        representation = "{}/{}".format(self.numerador, self.denominador)
        return representation

    def __repr__(self):
        representation = "Fracao({}, {})".format(self.numerador,
                                                self.denominador)
        return representation


# teste
if __name__ == '__main__':
    primeira = Fracao(42, 57)
    print(primeira)
    print(primeira.numerador, primeira.denominador)
