from django.urls import path
from .views import (
    RevolutAccounts,
    RevolutSpecificAccount,
    RevolutBalanceOnAccount,
    RevolutConfirmOrder,
    RevolutConfirmOrder,
    RevolutSendTransaction,
)

urlpatterns = [

    #Accounts
    path('accounts', RevolutAccounts.as_view(), name='list'),
    path('account/<int:pk>/', RevolutSpecificAccount.as_view(), name='list'),
    path('account/<int:pk>/balance', RevolutBalanceOnAccount.as_view(), name='list'),

    #Orders
    path('createOrder', RevolutConfirmOrder.as_view(), name='list'),
    path('confirmOrder', RevolutConfirmOrder.as_view(), name='create'),

    #Transactions

]
