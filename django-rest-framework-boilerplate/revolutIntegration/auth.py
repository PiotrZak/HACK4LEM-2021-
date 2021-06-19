import requests
import base64

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