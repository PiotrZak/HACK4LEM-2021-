from rest_framework import serializers
from django.db import models


class RevolutSerializer(serializers.ModelSerializer):

    def createOrder(self, validated_data):
        username = validated_data['amount']
        capture_mode = validated_data['capture_mode']
        merchant_order_ext_ref = validated_data['merchant_order_ext_ref']
        email = validated_data['email']
        currency = validated_data['currency']

        order_obj = CreateOrder(
            username=username,
            capture_mode=capture_mode,
            merchant_order_ext_ref=merchant_order_ext_ref,
            email=email,
            currency=currency,
        )
        return validated_data


class CreateOrder(models.Model):
    amount = models.IntegerField(max_length=30)
    capture_mode = models.CharField(max_length=30)
    merchant_order_ext_ref = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)
