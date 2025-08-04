import math


class Circulo:
    def __init__(self, diametro):
        self.__diametro = diametro

    @property
    def _diametro(self):
        return self.__diametro

    @_diametro.setter
    def _diametro(self, value):
        self.__diametro = value

    def calcula_radio(self):
        return self.__diametro / 2

    def calcular_area(self):
        return math.pi * self.calcula_radio() ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.calcula_radio()

    def __str__(self):
        return f"- Area: {self.calcular_area(): .2f}\n- Perimetro: {self.calcular_perimetro(): .2f}"


diametro = float(input("Diametro: "))
circulo = Circulo(diametro)
print(circulo)
