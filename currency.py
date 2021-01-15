from forex_python.converter import CurrencyRates


class CurrencyExchanger:

    currency = CurrencyRates()

    def get_brl_to_dolar_rate(self):
        dolar_to_brl_rate = round(self.currency.get_rate('USD', 'BRL'), 2)

        return dolar_to_brl_rate

    def convert_brl_to_dolar(self, amount):
        total = round(self.currency.convert('USD', 'BRL', amount), 2)

        return total


if __name__ == '__main__':
    exchanger = CurrencyExchanger()

    print(exchanger.get_brl_to_dolar_rate())
    print(exchanger.convert_brl_to_dolar(100))