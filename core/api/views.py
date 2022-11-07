from rest_framework.generics import ListAPIView
from core.models import Currency, Transactions, Category
from core.api.serializer import CurrencySerializer, CategorySerializer, WriteTransactionsSerializer, ReadTransactionsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None
class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class TransactionsModeldViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Transactions.objects.all()
    # serializer_class = TransactionsSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ("desc",)
    ordering_fields = ("amount",)

    def get_queryset(self):
        return Transactions.objects.select_related('currency','category','user').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list","retrieve"):
            return ReadTransactionsSerializer
        else:
            return WriteTransactionsSerializer

