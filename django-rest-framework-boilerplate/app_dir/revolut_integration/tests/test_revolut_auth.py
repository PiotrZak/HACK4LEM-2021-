from app_dir.revolut_integration import get_token_step1, get_token_step2
import pytest
import os


_DEVICE_ID = os.environ.get('REVOLUT_DEVICE_ID')
_TOKEN = os.environ.get('REVOLUT_TOKEN')
_SIMU_EXCHANGE = True  # True = Do not execute a real currency exchange
_SIMU_GET_TOKEN = True  # True = Do not try to get a real token
# (sms reception involved)

if _SIMU_GET_TOKEN is True:
    _PHONE = "+33612345678"
    _PASSWORD = "1234"
else:
    _PHONE = os.environ.get('REVOLUT_PHONE')
    _PASSWORD = os.environ.get('REVOLUT_TOKEN')

def test_get_token(capsys):
    _DEVICE_ID_TEST = "cli"
    get_token_step1(device_id=_DEVICE_ID_TEST,
                    phone=_PHONE,
                    password=_PASSWORD,
                    simulate=_SIMU_GET_TOKEN)

    if _SIMU_GET_TOKEN is True:
        code = "123456"
    else:
        with capsys.disabled():
            print()
            code = input(
                "Please enter the sms code sent to {} : ".format(_PHONE))