class Vendedor:
    def __init__(
        self, nombre, apellido, cedula, sexo, edad, sueldo_base, monto_vendido
    ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__sexo = sexo
        self.__edad = edad
        self.__sueldo_base = sueldo_base
        self.__monto_vendido = monto_vendido

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
    def _sexo(self):
        return self.__sexo

    @_sexo.setter
    def _sexo(self, value):
        self.__sexo = value

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _sueldo_base(self):
        return self.__sueldo_base

    @_sueldo_base.setter
    def _sueldo_base(self, value):
        self.__sueldo_base = value

    @property
    def _monto_vendido(self):
        return self.__monto_vendido

    @_monto_vendido.setter
    def _monto_vendido(self, value):
        self.__monto_vendido = value

    def get_porcentage_commision(self):
        if self.__monto_vendido > 0 and self.__monto_vendido < 7500:
            return 0.05
        elif self.__monto_vendido >= 9000 and self.__monto_vendido < 20000:
            return 0.07
        elif self.__monto_vendido >= 30000 and self.__monto_vendido < 100000:
            return 0.08
        elif self.__monto_vendido >= 150000:
            return 0.1
        return 0.06

    def get_bono_edad(self):
        if (self.__sexo == "M" and self.__edad == 55) or (
            self.__sexo == "H" and self.__edad == 65
        ):
            return 4000
        return 0

    def get_total(self):
        return (
            self.__sueldo_base
            + (self.get_porcentage_commision() * self.__monto_vendido)
            + self.get_bono_edad()
        )

    def __str__(self):
        return f"""El vendedor: {self.__nombre} - {self.__apellido} - {self.__cedula} - tiene
            un sueldo base de: {self.__sueldo_base} - tiene un monto vendido en el mes de: {self.__monto_vendido: .2f} y
            tiene un ingreso total de: {self.get_total(): .2f}
        """


nombre = input("Nombre: ")
apellido = input("Apellido: ")
cedula = input("cedula: ")
sueldo_base = float(input("Sueldo Base: "))
sexo = input("Sexo: ")
edad = int(input("Edad: "))
monto_vendido = float(input("Monto Vendido: "))
vendedor1 = Vendedor(nombre, apellido, cedula, sexo, edad, sueldo_base, monto_vendido)
print(vendedor1)
