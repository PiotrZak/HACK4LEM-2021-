from rest_framework import serializers
from app_dir.core.loading import get_model
from django.db import models

TABLE = get_model('revolut_integration', 'CreateOrder')

class RevolutSerializer(serializers.ModelSerializer):

    class Meta:
        model = TABLE
        fields = '__all__'

    def createOrder(self, validated_data):
        amount = validated_data['amgit  ount']
        capture_mode = validated_data['capture_mode']
        merchant_order_ext_ref = validated_data['merchant_order_ext_ref']
        email = validated_data['email']
        currency = validated_data['currency']

        order_obj = CreateOrder(
            amount=amount,
            capture_mode=capture_mode,
            merchant_order_ext_ref=merchant_order_ext_ref,
            email=email,
            currency=currency,
        )
        return validated_data
