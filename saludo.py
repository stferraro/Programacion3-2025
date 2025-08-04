class Saludo:
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.nombre}, {self.mensaje}!"

    def __repr__(self):
        return f"Saludo(nombre={self.nombre!r}, mensaje={self.mensaje!r})"


if __name__ == "__main__":
    nombre = input("Introduce tu nombre: ")
    mensaje = input("Introduce un mensaje: ")
    saludo = Saludo(nombre, mensaje)
    print(saludo)
