from django.db import models


class RevolutTransaction(models.Model):
    senderMail = models.CharField(max_length=30)
    recipientMail = models.CharField(max_length=30)
    amount = models.IntegerField(max_length=30)


class RevolutAccountBalance:
    AMOUNT = models.IntegerField(max_length=30)


class RevolutAccount(models.Model):
    id = models.IntegerField(max_length=30)
    name = models.CharField(max_length=30)
    balance = models.IntegerField(max_length=30)
    currency = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    public = models.BooleanField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class CreateOrder(models.Model):
    amount = models.IntegerField(max_length=30)
    capture_mode = models.CharField(max_length=30)
    merchant_order_ext_ref = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)
