import logging
from collections import defaultdict
from datetime import datetime

from pydollar_vzla.dolar_price import DolarPrice

_logger = logging.getLogger(__name__)


class ExchangeRate:
    """
    Uses PyDollar-VZLA to fetch USD and EUR exchange rates from BCV.
    """

    @staticmethod
    def _scrap(available_currencies):
        """
        Fetch exchange rates for given currencies using PyDollar-VZLA (BCV source).

        Args:
            available_currencies (list): e.g. ['USD']

        Returns:
            dict: { 'USD': (rate: float, date: datetime.date), ... }
        """
        result = {}
        date = datetime.today().date()

        try:
            dolar_data = DolarPrice().get_all_dolar_prices()
            print("DEBUG dolar_data:", dolar_data)
            print("DEBUG dolar_data keys:", list(dolar_data.keys()))
        except Exception as e:
            _logger.error("Failed to fetch rates from PyDollar-VZLA: %s", e)
            return result

        for currency in available_currencies:
            try:
                if currency in ["Bs", "VES", "VEF", "VED"]:
                    result[currency] = (1.0, date)
                elif currency == "USD":
                    # Aquí puedes ajustar la clave según el resultado del print
                    rate = float(dolar_data["bcv"])  # Cambia 'bcv' si es necesario
                    result[currency] = (rate, date)
                else:
                    _logger.warning(
                        "Currency %s is not supported by PyDollar-VZLA.", currency
                    )
            except Exception as e:
                _logger.warning("Error processing rate for %s: %s", currency, e)

        return result

    @staticmethod
    def obtain_rates(base_currency, currencies, date_from=None, date_to=None):
        """
        Returns a dictionary of exchange rates formatted for Odoo-like structures.

        Returns:
            dict: {
                'YYYY-MM-DD': {
                    'USD': rate,
                    ...
                }
            }
        """
        content = defaultdict(dict)
        bcv_data = ExchangeRate._scrap(currencies)

        for currency, (rate, date) in bcv_data.items():
            date_str = date.isoformat()
            content[date_str][currency] = rate

        return content


# Test block (executed only when running this script directly)
if __name__ == "__main__":
    print("Fetching exchange rates from BCV using PyDollar-VZLA...\n")
    currencies = ["USD"]
    rates = ExchangeRate.obtain_rates(base_currency="USD", currencies=currencies)

    for date_str, currency_data in rates.items():
        print(f"Date: {date_str}")
        for currency, rate in currency_data.items():
            print(f"  {currency}: {rate}")
