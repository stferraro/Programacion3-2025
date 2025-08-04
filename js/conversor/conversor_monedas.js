// Conversor_monedas.js
class ConversorMonedas {
  #bolivar;
  #dolar;
  #euro;
  #tasaCambio;

  constructor(euro, dolar) {
    this.#bolivar = 0;
    this.#dolar = dolar;
    this.#euro = euro;
  }

  get tasaCambio() {
    return this.#tasaCambio;
  }

  set tasaCambio(tasa) {
    this.#tasaCambio = tasa;
  }

  get bolivar() {
    return this.#bolivar;
  }

  set bolivar(monto) {
    this.#bolivar = monto;
  }

  get dolar() {
    return this.#dolar;
  }
  set dolar(monto) {
    this.#dolar = monto;
  }

  get euro() {
    return this.#euro;
  }
  set euro(monto) {
    this.#euro = monto;
  }

  calcularDolar(bolivares) {
    this.#dolar = bolivares / this.#tasaCambio.dolar;
    return this.#dolar;
  }

  calcularEuro(bolivares) {
    this.#euro = bolivares / this.#tasaCambio.euro;
    return this.#euro;
  }

  toString() {
    const dolares = this.calcularDolar(this.#bolivar);
    const euros = this.calcularEuro(this.#bolivar);
    return `Bolívares: ${this.#bolivar}
        Dólares: ${dolares.toFixed(2)}
        Euros: ${euros.toFixed(2)}
        Tasa de Cambio: Dólar = ${this.#tasaCambio.dolar}, Euro = ${
      this.#tasaCambio.euro
    }`;
  }
}

const bolivares = parseFloat(prompt("Ingrese la cantidad en bolívares:"));
const tasaCambioDolar = parseFloat(prompt("Ingrese la tasa del dólar:"));
const tasaCambioEuro = parseFloat(prompt("Ingrese la tasa del euro:"));

const conversor = new ConversorMonedas(tasaCambioEuro, tasaCambioDolar);
conversor.bolivar = bolivares; // Asigna los bolívares
conversor.tasaCambio = { dolar: tasaCambioDolar, euro: tasaCambioEuro }; // Asigna la tasa de cambio

alert(conversor.toString());
console.log(conversor.toString());
