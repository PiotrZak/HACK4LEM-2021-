from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from .serializers import RevolutSerializer
from ....models import RevolutAccount, CreateOrder, RevolutAccountBalance, RevolutTransaction


class RevolutAccounts(ListAPIView):
    serializer_class = RevolutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RevolutAccount.objects.all()


class RevolutSpecificAccount(ListAPIView):
    queryset = RevolutAccount.objects.all()
    serializer_class = RevolutSerializer


class RevolutBalanceOnAccount(ListAPIView):
    queryset = RevolutAccountBalance.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RevolutSerializer


class RevolutSendTransaction(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RevolutTransaction.objects.all()
    serializer_class = RevolutSerializer


class RevolutCreateOrder(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CreateOrder.objects.all()
    serializer_class = RevolutSerializer


