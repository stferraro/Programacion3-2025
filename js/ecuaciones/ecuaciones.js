class Ecuaciones {
  #a;
  #b;
  #c;

  constructor(a, b, c) {
    this.#a = a;
    this.#b = b;
    this.#c = c;
  }

  get a() {
    return this.#a;
  }

  get b() {
    return this.#b;
  }

  get c() {
    return this.#c;
  }

  set a(value) {
    this.#a = value;
  }

  set b(value) {
    this.#b = value;
  }

  set c(value) {
    this.#c = value;
  }

  get solucionX1() {
    const discriminante = this.#b ** 2 - 4 * this.#a * this.#c;
    if (discriminante < 0) {
      return null; // No hay solución real
    }
    return (-this.#b + Math.sqrt(discriminante)) / (2 * this.#a);
  }

  get solucionX2() {
    const discriminante = this.#b ** 2 - 4 * this.#a * this.#c;
    if (discriminante < 0) {
      return null; // No hay solución real
    }
    return (-this.#b - Math.sqrt(discriminante)) / (2 * this.#a);
  }

  toString() {
    return `Ecuación: ${this.#a}x² + ${this.#b}x + ${
      this.#c
    } = 0, Soluciones: x1 = ${this.solucionX1.toFixed(
      2
    )}, x2 = ${this.solucionX2.toFixed(2)}`;
  }
}

const a = parseFloat(prompt("Ingrese el valor del coeficiente a: "));
const b = parseFloat(prompt("Ingrese el valor del coeficiente b: "));
const c = parseFloat(prompt("Ingrese el valor del coeficiente c: "));
const ecuacion = new Ecuaciones(a, b, c);
alert(ecuacion.toString());
