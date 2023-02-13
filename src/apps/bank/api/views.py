from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.bank.models import CurrencyModel, CategoryModel, TransactionModel
from apps.bank.api.serializers import CurrencySerializer, CategorySerializer, TransactionSerializer

class CurrencyModelViewSet(ModelViewSet):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class TransactionModelViewSet(ModelViewSet):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer