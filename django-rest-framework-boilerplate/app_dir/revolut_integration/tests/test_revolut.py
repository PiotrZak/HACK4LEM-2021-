from app_dir.revolut_integration import Amount, Revolut
import pytest
import os

_DEVICE_ID = os.environ.get('REVOLUT_DEVICE_ID')
#_TOKEN = os.environ.get('REVOLUT_TOKEN')
_TOKEN = "sk_i0rL5l6ZjvyuiFclBUMULeOleotfEmrLEn4kgLGNuUUQ0puQNUuT1A9wmKo0jfV6"

revolut = Revolut(token=_TOKEN, device_id=_DEVICE_ID)

def test_class_Amount():
    amount = Amount(revolut_amount=100, currency="EUR")
    assert amount.real_amount == 1
    assert str(amount) == "1.00 EUR"

    amount = Amount(real_amount=1, currency="EUR")
    assert amount.revolut_amount == 100
    assert str(amount) == "1.00 EUR"


def test_class_Amount_errors():
    with pytest.raises(KeyError):
        Amount(revolut_amount=100, currency="UNKNOWN")

    with pytest.raises(TypeError):
        Amount(revolut_amount="abc", currency="BTC")

    with pytest.raises(TypeError):
        Amount(real_amount="def", currency="EUR")

    with pytest.raises(ValueError):
        Amount(currency="BTC")
