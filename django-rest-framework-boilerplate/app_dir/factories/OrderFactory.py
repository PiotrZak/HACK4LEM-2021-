import factory
from faker import Factory

from app_dir.revolut_integration_models import CreateOrder

faker = Factory.create()


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = CreateOrder

        amount = faker.amount()
        capture_mode = faker.capture_mode()
        merchant_order_ext_ref = faker.merchant_order_ext_ref()
        email = faker.email()
        currency = faker.currency()
