class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c, altura):
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.__altura = altura

    @property
    def _lado_a(self):
        return self.__lado_a

    @_lado_a.setter
    def _lado_a(self, value):
        self.__lado_a = value

    @property
    def _lado_b(self):
        return self.__lado_b

    @_lado_b.setter
    def _lado_b(self, value):
        self.__lado_b = value

    @property
    def _lado_c(self):
        return self.__lado_c

    @_lado_c.setter
    def _lado_c(self, value):
        self.__lado_c = value

    def es_valido(self):
        if (
            (self.__lado_a + self.__lado_b > self.__lado_c)
            and (self.__lado_a + self.__lado_c > self.__lado_b)
            and (self.__lado_b + self.__lado_c > self.__lado_a)
        ):
            return True
        return False

    def calcula_area(self):
        if self.es_valido():
            return self.__lado_b * self.__altura / 2

    def calcula_perimetro(self):
        if self.es_valido():
            return self.__lado_a + self.__lado_b + self.__lado_c

    def __str__(self):
        if self.es_valido():
            return (
                f"Area: {self.calcula_area(): .2f}cm\n"
                f"Perimetro: {self.calcula_perimetro(): .2f}cm"
            )
        return "No es un Triangulo"


triangulo = Triangulo(4, 6, 10, 20)
print(triangulo)
triangulo2 = Triangulo(5, 6, 8, 7)
print(triangulo2)
