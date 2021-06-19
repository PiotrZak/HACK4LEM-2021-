from rest_framework import serializers
from django.contrib.auth import get_user_model



class RevolutSerializer(serializers.ModelSerializer):



    class Meta:
        model = CreateOrder
        fields = [
            'amount',
            'capture_mode',
            'merchant_order_ext_ref',
            'email',
            'currency',
        ]

        model =








    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
            is_staff=True
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
