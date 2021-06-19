import requests
import base64
import json

API_BASE = "https://api.revolut.com"

MERCHANT_URL = "https://merchant.revolut.com/api/1.0/orders"
_URL_GET_TOKEN_STEP1 = API_BASE + "/signin"
_URL_GET_TOKEN_STEP2 = API_BASE + "/signin/confirm"

_DEFAULT_TOKEN_FOR_SIGNIN = "sk_i0rL5l6ZjvyuiFclBUMULeOleotfEmrLEn4kgLGNuUUQ0puQNUuT1A9wmKo0jfV6"


class Client:

    def __init__(self, token, device_id):
        self.session = requests.session()
        self.session.headers = {
            'Host': 'api.revolut.com',
            'X-Api-Version': '1',
            'X-Client-Version': '6.34.3',
            'X-Device-Id': device_id,
            'User-Agent': 'Revolut/5.5 500500250 (CLI; Android 4.4.2)',
            'Authorization': 'Basic ' + token,
        }

    def _get(self, url, *, expected_status_code=200, **kwargs):
        ret = self.session.get(url=url, **kwargs)
        if ret.status.code != expected_status_code:
            raise ConnectionError(
                'Status code {} for url {}\n{}'.format(
                    ret.status_code, url, ret.text))
        return ret

    def _post(self, url, *, expected_status_code=200, **kwargs):
        ret = self.session.post(url=url, **kwargs)
        if ret.status_code != expected_status_code:
            raise ConnectionError(
                'Status code {} for url {}\n{}'.format(
                    ret.status_code, url, ret.text))
        return ret

def get_token_1(device_id, phone, password, simulate=False):
    if simulate:
        return "SMS"

    c = Client(device_id=device_id, token=_DEFAULT_TOKEN_FOR_SIGNIN)
    data = {"phone": phone, "password": password}
    ret = c._post(_URL_GET_TOKEN_STEP1, json=data)
    channel = ret.json().get("channel")
    return channel


def get_token_2(device_id, phone, code, simulate=False):
    """ Function to obtain a Revolut token (step 2 : with code) """
    if simulate:
        simu = '{"user":{"id":"fakeuserid","createdDate":123456789,\
        "address":{"city":"my_city","country":"FR","postcode":"12345",\
        "region":"my_region","streetLine1":"1 rue mon adresse",\
        "streetLine2":"Appt 1"},\"birthDate":[1980,1,1],"firstName":"John",\
        "lastName":"Doe","phone":"+33612345678","email":"myemail@email.com",\
        "emailVerified":false,"state":"ACTIVE","referralCode":"refcode",\
        "kyc":"PASSED","termsVersion":"2018-05-25","underReview":false,\
        "riskAssessed":false,"locale":"en-GB"},"wallet":{"id":"wallet_id",\
        "ref":"12345678","state":"ACTIVE","baseCurrency":"EUR",\
        "topupLimit":3000000,"totalTopup":0,"topupResetDate":123456789,\
        "pockets":[{"id":"pocket_id","type":"CURRENT","state":"ACTIVE",\
        "currency":"EUR","balance":100,"blockedAmount":0,"closed":false,\
        "creditLimit":0}]},"accessToken":"myaccesstoken"}'
        raw_get_token = json.loads(simu)
    else:
        c = Client(device_id=device_id, token=_DEFAULT_TOKEN_FOR_SIGNIN)
        code = code.replace("-", "")  # If the user would put -
        data = {"phone": phone, "code": code}
        ret = c._post(_URL_GET_TOKEN_STEP2, json=data)
        raw_get_token = ret.json()
    return raw_get_token


def extract_token(json_response):
    user_id = json_response["user"]["id"]
    access_token = json_response["accessToken"]
    token_to_encode = "{}:{}".format(user_id, access_token).encode("ascii")
    # Ascii encoding required by b64encode function : 8 bits char as input
    token = base64.b64encode(token_to_encode)
    return token.decode("ascii")


def signin_biometric(device_id, phone, access_token, selfie_filepath):
    files = {"selfie": open(selfie_filepath, "rb")}
    c = Client(device_id=device_id, token=_DEFAULT_TOKEN_FOR_SIGNIN)
    c.session.auth = (phone, access_token)
    res = c._post(API_BASE + "/biometric-signin/selfie", files=files)
    biometric_id = res.json()["id"]
    res = c._post(API_BASE + "/biometric-signin/confirm/" + biometric_id)
    return res.json()
