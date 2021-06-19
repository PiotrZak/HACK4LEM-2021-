import factory
from faker import Factory
from ..core.loading import get_model

faker = Factory.create()


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('revolut_integration', 'CreateOrder');

        amount = faker.amount()
        capture_mode = faker.capture_mode()
        merchant_order_ext_ref = faker.merchant_order_ext_ref()
        email = faker.email()
        currency = faker.currency()
