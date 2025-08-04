class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def _base(self):
        return self.__base

    @_base.setter
    def _base(self, value):
        self.__base = value

    @property
    def _altura(self):
        return self.__altura

    @_altura.setter
    def _altura(self, value):
        self.__altura = value

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return (self.__base + self.__altura) * 2

    def __str__(self):
        return (
            f"- Area: {self.calcular_area(): .2f}\n"
            f"- Perimetro: {self.calcular_perimetro(): .2f}"
        )


base = float(input("base: "))
altura = float(input("altura: "))

rectangulo = Rectangulo(base, altura)

print(rectangulo)
