import math


class Cilindro:
    def __init__(self, diametro, altura):
        self.__diametro = diametro
        self.__altura = altura

    def calcular_area(self):
        return (self.__diametro / 2**2) * math.pi

    def calcular_volumen(self):
        return (self.__diametro / 2**2) * math.pi * self.__altura

    def __str__(self):
        return (
            f"Area: {self.calcular_area(): .2f}\n"
            f"Volumen: {self.calcular_volumen(): .2f}"
        )


diametro = float(input("Diametro del cilindro: "))
altura = float(input("Altura del cilindro: "))
cilindro = Cilindro(diametro, altura)
print(cilindro)
