import base64
from datetime import datetime
import json
import requests

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

class Account

    def __init__(self, currency, revolut_amount=None, realAmount=None):
        if currency not in _AVAILABLE_CURRENCIES:
            raise KeyError(currency)
        self.currency = currency

class Transaction:
    def __init__(self, from, to, date):

        if type(from) != Amount:
            raise TypeError
        if type(to) != Amount:
            raise TypeError
        if type(date) != datetime:
            raise TypeError

        self.from = from
        self.to = to
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
        if type(revolut_amount) != int:
            raise TypeError


