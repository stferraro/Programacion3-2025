from boleto import Boleto
from persona import Persona

nombre = input("Nombre: ")
apellido = input("Apellido: ")
cedula = input("Cedula: ")
edad = int(input("Edad: "))

persona = Persona(nombre, apellido, cedula, edad)
print(persona)

boleto = Boleto(persona)
print(boleto)
