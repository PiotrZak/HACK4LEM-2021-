from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import OrderFactory

faker = Factory.create()


class CreateOrderRevolut(TestCase):
    def setUp(self):
        self.order = OrderFactory()
        self.client = APIClient()

        self.namespace = 'revolut_integration_api'
        self body = {
            'amount': faker.amount(),
            'capture_mode': faker.capture_mode(),
            'merchant_order_ext_ref': faker.merchant_order_ext_ref(),
            'email': faker.email(),
            'currency': faker.currency(),
        }

        self.create_url = reverse(self.namespace + ':create-order')

    def test_create_order(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(201, response.status_code)