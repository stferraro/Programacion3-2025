from saludo import Saludo


def test_str():
    s = Saludo("Juan", "Hola")
    assert str(s) == "Juan, Hola!"
