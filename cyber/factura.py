from cliente import Cliente


class Factura:
    def __init__(self, cliente):
        self.__cliente = cliente

    @property
    def _cliente(self):
        return self.__cliente

    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value

    def get_calcula_valor(self):
        if 60 <= self.__cliente._minutos_conectados <= 90:
            return 10
        elif 40 <= self.__cliente._minutos_conectados <= 59:
            return 8
        elif 20 <= self.__cliente._minutos_conectados <= 39:
            return 5
        elif self.__cliente._minutos_conectados < 20:
            return 3
        return 0

    def __str__(self):
        return f"{self.__cliente.__str__()}\n{self.get_calcula_valor(): .2f}$$"


nombre = input("Nombre: ")
apellido = input("Apellido: ")
maquina_asignada = int(input("Maquina Asignda: "))
minutos_conectados = float(input("Minutos Conectados: "))
cliente = Cliente(nombre, apellido, maquina_asignada, minutos_conectados)
factura = Factura(cliente)
print(factura)
