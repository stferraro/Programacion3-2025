class CalculadorOperaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "no se puede hacer una division entre 0"


calculadora = CalculadorOperaciones(5, 6)
c = calculadora.suma()
d = calculadora.resta()
f = calculadora.dividir()
s = calculadora.multiplicar()
print(c, d, f, s)
print(f"{c: .2f} - {d: .3f} - {f: .4f} - {s: .2f}")
