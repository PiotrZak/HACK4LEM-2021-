from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from .serializers import RevolutSerializer
from ....models import RevolutAccount, CreateOrder, RevolutAccountBalance


class RevolutAccounts(CreateAPIView):
    serializer_class = RevolutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RevolutAccount.objects.all()


class RevolutSpecificAccount(RetrieveAPIView):
    queryset = RevolutAccount.objects.all()
    serializer_class = RevolutSerializer


class RevolutBalanceOnAccount(DestroyAPIView):
    queryset = RevolutAccountBalance.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RevolutSerializer


class RevolutSendTransaction(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = RevolutSerializer

class RevolutCreateOrder(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =

