class Cono {
  #diametro;
  #generatriz;

  constructor(diametro, generatriz) {
    this.#diametro = diametro;
    this.#generatriz = generatriz;
  }

  get diametro() {
    return this.#diametro;
  }

  set diametro(value) {
    this.#diametro = value;
  }

  get generatriz() {
    return this.#generatriz;
  }

  set generatriz(value) {
    this.#generatriz = value;
  }

  area_cono() {
    return (
      (this.#diametro / 2) * Math.PI * (this.#diametro / 2 + this.#generatriz)
    );
  }

  altura_cono() {
    return Math.sqrt(this.#generatriz ** 2 - (this.#diametro / 2) ** 2);
  }

  volumen_cono() {
    return (1 / 3) * (Math.PI * (this.#diametro / 2) ** 2 * this.altura_cono());
  }

  toString() {
    return (
      `El Cono de Diametro ${this.#diametro} y Generatriz: ${
        this.#generatriz
      } tiene un area y un volumen de: ` +
      `\nArea: ${this.area_cono().toFixed(
        2
      )}\nVolumen:${this.volumen_cono().toFixed(2)}`
    );
  }
}

const diametro = parseFloat(
  prompt(`Introduce el valor del diametro del cono: `)
);
const generatriz = parseFloat(
  prompt(`Introduce el valor de la generatriz del cono: `)
);
const cono = new Cono(diametro, generatriz);
alert(cono.toString());
