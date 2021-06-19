from app_dir.revolut_integration.auth import Client
from tensorflow import keras

API_BASE_ORIGINAL = "https://api.revolut.com"
API_BASE = "https://sandbox-business.revolut.com"



SANDBOX_API_KEY = "sk_IbM8arw0C8vt93eR1kdzs6yO1WPpVjuDGbHuq8A9BcJDD_K9lLoZ0F9nqhXLiQv1"

CONFIRM_ORDER = API_BASE + "/api/1.0/orders"
VERIFICATION_PROVIDERS = ['pko', 'plus', 'vw']

class ProcessOrders:
    def __init__(self, token, device_id, userBalance, amount, orderId, date, aiApproved):

        if type(amount) != Amount:
            raise TypeError
        if type(date) != datetime:
            raise TypeError
        if type(date) != bool:
            raise TypeError

        self.client = Client(token=token, device_id=device_id)
        self.orderId = orderId
        self.userBalance = userBalance
        self.amount = amount
        self.date = date
        self.aiApproved = aiApproved

# todo
# verify how can get payment_method_id?

    def verify_transaction(aiApproved=False, orderId, payment_method_id, userBalance, amount):

        model = keras.models.load_model('../../../hack4lem.h5')

        #todo - how is constructed ml model? - debug session

        if aiApproved:
            if userBalance > amount:
                ret = confirm_order(orderId, payment_method_id)
                order_details = ret.json();

        return order_details;

    def createOrder(self):
        ret = self.client._post(CREATE_ORDER, )
        ret = ret.json();

    def initiate_order(self, ):
        #todo - initiate order when email appear

    def confirm_order(self, orderId, payment_method_id):

        ret = self.client._post(CONFIRM_ORDER, orderId, payment_method_id)
        ret = ret.json();

        return ret;

















