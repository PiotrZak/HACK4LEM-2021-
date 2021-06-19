from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from .serializers import RevolutSerializer
from ...core.pagination import PostLimitOffsetPagination

from ....models import RevolutAccount, CreateOrder, RevolutAccountBalance, RevolutTransaction

permission_classes = [IsAuthenticatedOrReadOnly]
serializer_class = UserSerializer
pagination_class = PostLimitOffsetPagination


class RevolutListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RevolutSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(username__icontains=query)
            )

        return queryset_list.order_by('-id')

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


