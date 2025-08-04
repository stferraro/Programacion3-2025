class Cliente:
    def __init__(self, nombre, apellido, maquina_asignada, minutos_conectados):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__maquina_asignada = maquina_asignada
        self.__minutos_conectados = minutos_conectados

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
    def _maquina_asignada(self):
        return self.__maquina_asignada

    @_maquina_asignada.setter
    def _maquina_asignada(self, value):
        self.__maquina_asignada = value

    @property
    def _minutos_conectados(self):
        return self.__minutos_conectados

    @_minutos_conectados.setter
    def _minutos_conectados(self, value):
        self.__minutos_conectados = value

    def __str__(self):
        return (
            f"** Datos del estudiante **\n"
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"Maquina Asignada: {self.__maquina_asignada}\n"
            f"Minutos de conexión: {self.__minutos_conectados}"
        )
