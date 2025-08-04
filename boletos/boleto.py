class Boleto:
    def __init__(self, persona):
        self.__persona = persona

    @property
    def _persona(self):
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    def __get_costo_boleto(self):
        if self.__persona._edad >= 0 and self.__persona._edad <= 5:
            return 0
        elif self.__persona._edad > 5 and self.__persona._edad <= 15:
            return 25
        elif self.__persona._edad > 15 and self.__persona._edad <= 45:
            return 75
        elif self.__persona._edad > 45 and self.__persona._edad <= 65:
            return 50
        else:
            return 40

    def __get_costo_total_boleto(self):
        return self.__get_costo_boleto() * 1.16

    def __str__(self):
        return (
            f"\nEl costo del boleto de la persona es: \n{self.__persona}\n"
            f"Costo: {self.__get_costo_total_boleto(): .2f} $$"
        )
