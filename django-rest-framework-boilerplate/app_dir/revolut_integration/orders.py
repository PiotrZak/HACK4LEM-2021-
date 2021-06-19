import requests
import base64
import json

from app_dir.revolut_integration import Transaction
from app_dir.revolut_integration.auth import Client

API_BASE = "https://api.revolut.com"
CONFIRM_ORDER = API_BASE + "/api/1.0/orders"

class ProcessOrders:
    def __init__(self, token, device_id, userBalance, amount, orderId, date, aiApproved):

        if type(amount) != Amount:
            raise TypeError
        if type(to_amount) != Amount:
            raise TypeError
        if type(date) != datetime:
            raise TypeError
        if type(date) != bool:
            raise TypeError

        self.client = Client(token=token, device_id=device_id)
        self.orderId = orderId
        self.userBalance = userBalance
        self.from_amount = from_amount
        self.to_amount = to_amount
        self.date = date
        self.aiApproved = aiApproved

# todo
# integrate model - which return 100 on score

# todo
# verify how can get payment_method_id?
    
    def verify_transaction(aiApproved=False, orderId, payment_method_id, userBalance, amount):
        if aiApproved:
            if userBalance > amount:
                ret = confirm_order(orderId, payment_method_id)

                order_details = ret.json();

        return order_details;


    def initiate_order(self, ):

    def confirm_order(self, orderId, payment_method_id):

        ret = self.client._post(CONFIRM_ORDER)
        raw_accounts = ret.json();

        account_balances = []

















