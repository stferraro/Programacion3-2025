class EstudianteUniversitario:
    def __init__(
        self, nombre, apellido, cedula, codigo_universitario, semestre, promedio_notas
    ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__codigo_universitario = codigo_universitario
        self.__semestre = semestre
        self.__promedio_notas = promedio_notas

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
    def _codigo_universitario(self):
        return self.__codigo_universitario

    @_codigo_universitario.setter
    def _codigo_universitario(self, value):
        self.__codigo_universitario = value

    @property
    def _semestre(self):
        return self.__semestre

    @_semestre.setter
    def _semestre(self, value):
        self.__semestre = value

    @property
    def _promedio_notas(self):
        return self.__promedio_notas

    @_promedio_notas.setter
    def _promedio_notas(self, value):
        self.__promedio_notas = value

    def get_nivel(self):
        if self.__promedio_notas == 20:
            return "eximido"
        elif self.__promedio_notas >= 16 and self.__promedio_notas < 20:
            return "excelente"
        elif self.__promedio_notas >= 13 and self.__promedio_notas < 16:
            return "mas que suficiente"
        elif self.__promedio_notas >= 10 and self.__promedio_notas < 13:
            return "suficiente"
        elif self.__promedio_notas <= 9:
            return "insuficiente"
        return "valor errado"

    def __str__(self):
        return (
            f"** Datos del estudiante **\n"
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"Cédula: {self.__cedula}\n"
            f"Código Universitario: {self.__codigo_universitario}\n"
            f"Semestre: {self.__semestre}\n"
            f"Promedio de Notas: {self.__promedio_notas}\n"
            f"Nivel: {self.get_nivel()}"
        )


nombre = input("Nombre: ")
apellido = input("Apellido: ")
cedula = input("cedula: ")
codigo_universitario = input("Codigo Universitario: ")
semestre = input("Semestre: ")
promedio_notas = float(input("Promedio de Notas: "))
estudiante = EstudianteUniversitario(
    nombre, apellido, cedula, codigo_universitario, semestre, promedio_notas
)
print(estudiante)
