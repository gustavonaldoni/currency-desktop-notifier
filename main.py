from currency import CurrencyExchanger
from notifier import Notifier

icon_path = './icon.ico'

notifier = Notifier(icon_path)

exchanger = CurrencyExchanger()
brl_to_dolar_rate = exchanger.get_brl_to_dolar_rate()

default_title = 'A new rate was found!'
default_message = f'OMG! We have discovered that 1 USD = {brl_to_dolar_rate} BRL.'

notifier.show_notification_endless(default_title, default_message, 10)