class Circulo {
  #diametro;

  constructor(diametro) {
    this.#diametro = diametro;
  }

  get diametro() {
    return this.#diametro;
  }

  set diametro(value) {
    this.#diametro = value;
  }

  get radio() {
    return this.#diametro / 2;
  }

  calcularArea() {
    return (Math.PI * this.#diametro) / 2 ** 2;
  }

  calcularPerimetro() {
    return Math.PI * this.#diametro;
  }

  toString() {
    return `Diámetro: ${this.#diametro}, Radio: ${
      this.radio
    }, Área: ${this.calcularArea().toFixed(
      2
    )}, Perímetro: ${this.calcularPerimetro().toFixed(2)}`;
  }
}
const diametro = parseFloat(prompt("Ingrese el diámetro del círculo: "));
const circulo = new Circulo(diametro);
alert(circulo.toString());
