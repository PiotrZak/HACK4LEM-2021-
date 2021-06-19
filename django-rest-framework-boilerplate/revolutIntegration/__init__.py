
from datetime import datetime

from urllib.parse import urljoin

API_BASE = "https://api.revolut.com"
_URL_GET_ACCOUNTS = API_BASE + "/user/current/wallet"
_URL_GET_TRANSACTIONS_LAST = API_BASE + "/user/current/transactions/last"
_URL_QUOTE = API_BASE + "/quote/"
_URL_EXCHANGE = API_BASE + "/exchange"
_URL_GET_TOKEN_STEP1 = API_BASE + "/signin"
_URL_GET_TOKEN_STEP2 = API_BASE + "/signin/confirm"

_AVAILABLE_CURRENCIES = ["USD", "RON", "HUF", "CZK", "GBP", "CAD", "THB",
                         "SGD", "CHF", "AUD", "ILS", "DKK", "PLN", "MAD",
                         "AED", "EUR", "JPY", "ZAR", "NZD", "HKD", "TRY",
                         "QAR", "NOK", "SEK", "BTC", "ETH", "XRP", "BCH",
                         "LTC", "SAR", "RUB", "RSD", "MXN", "ISK", "HRK",
                         "BGN", "XAU", "IDR", "INR", "MYR", "PHP", "XLM",
                         "EOS", "OMG", "XTZ", "ZRX"]

_CRYPTO = ["BTC", "ETH", "BCH", "XRP", "LTC"]

# The amounts are stored as integer on Revolut.
# They apply a scale factor depending on the currency
_DEFAULT_SCALE_FACTOR = 100
_SCALE_FACTOR_CURRENCY_DICT = {
    "EUR": 100,
    "BTC": 100000000,
    "ETH": 100000000,
    "BCH": 100000000,
    "XRP": 100000000,
    "LTC": 100000000,
}


class Account:

    def __init__(self, currency, revolut_amount=None, realAmount=None):
        if currency not in _AVAILABLE_CURRENCIES:
            raise KeyError(currency)
        self.currency = currency


class Transaction:
    def __init__(self, from_amount, to_amount, date):

        if type(from_amount) != Amount:
            raise TypeError
        if type(to_amount) != Amount:
            raise TypeError
        if type(date) != datetime:
            raise TypeError

        self.from_amount = from_amount
        self.to_amount = to_amount
        self.date = date

        def __str__(self):
            return ('({}) {} => {}'.format(self.date.strftime("%d/%m/%Y %H:%M:%S"),
                                           self.from_amount,
                                           self.to_amount))


class Amount:

    def __init__(self, currency, revolut_amount=None, real_amount=None):
        if currency not in _AVAILABLE_CURRENCIES:
            raise KeyError(currency)
        self.currency = currency

        if revolut_amount is not None:
            if type(revolut_amount) != int:
                raise TypeError

        elif real_amount is not None:
            if type(real_amount) != int:
                raise TypeError
        else:
            raise ValueError("amounts need be set")

    def get_real_amount(self):

        scale = _SCALE_FACTOR_CURRENCY_DICT.get(
            self.currency, _DEFAULT_SCALE_FACTOR)
        return float(self.revolut_amount / scale)

    def get_revolut_amount(self):

        scale = _SCALE_FACTOR_CURRENCY_DICT.get(
            self.currency, _DEFAULT_SCALE_FACTOR)
        return int(self.real_amount * scale)
