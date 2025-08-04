class Persona:
    def __init__(self, nombre, apellido, cedula, edad):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__edad = edad

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    def __str__(self):
        return (
            f"Nombre: {self.__nombre}\nApellido: {self.__apellido}\n"
            f"Cedula: {self.__cedula}\nEdad: {self.__edad}"
        )
