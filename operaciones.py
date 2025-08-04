def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "no se puede hacer una division entre 0"


a = float(input("a: "))
b = float(input("b: "))
c = suma(a, b)
d = multiplicar(a, b)
e = dividir(a, b)
f = float(input("f: "))
s = float(input("s: "))
h = resta(f, s)
print(c, d, e, h)
r = "mi nombre es Gerardo"
