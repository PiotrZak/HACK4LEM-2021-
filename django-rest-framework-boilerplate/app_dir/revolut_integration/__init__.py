from datetime import datetime
from app_dir.revolut_integration.auth import Client


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


class Revolut:
    def __init__(self, token, device_id):
        self.client = Client(token=token, device_id=device_id)

    def get_account_balances(self):
        ret = self.client._get(_URL_GET_ACCOUNTS)
        raw_accounts = ret.json();

        account_balances = []

        for raw_account in raw_accounts.get("pockets"):
            account_balances.append({
                "balance": raw_account.get("balance"),
                "currency": raw_account.get("currency"),
                "type": raw_account.get("type"),
                "state": raw_account.get("state"),
                "vault_name": raw_account.get("name", ""),
            })

        self.get_account_balances = Accounts(account_balances)
        return self.get_account_balances;


class Accounts:

    def __init__(self, account_balances):
        self.raw_list = account_balances
        self.list = [
            Account(
                account_type=account.get("type"),
                balance=Amount(
                    currency=account.get("currency"),
                    revolut_amount=account.get("balance"),
                ),
                state=account.get("state"),
                vault_name=account.get("vault_name"),
            )
            for account in self.raw_list
        ]


class Account:

    def __init__(self, account_type, balance, state, vault_name):
        self.account_type = account_type  # CURRENT, SAVINGS
        self.balance = balance
        self.state = state  # ACTIVE, INACTIVE
        self.vault_name = vault_name
        self.name = self.build_account_name()

    def build_account_name(self):
        if self.account_type == _VAULT_ACCOUNT_TYPE:
            account_name = '{currency} {type} ({vault_name})'.format(
                currency=self.balance.currency,
                type=self.account_type,
                vault_name=self.vault_name)
        else:
            account_name = '{currency} {type}'.format(
                currency=self.balance.currency,
                type=self.account_type)
        return account_name

    def __str__(self):
        return "{name} : {balance}".format(name=self.name,
                                           balance=str(self.balance))


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
