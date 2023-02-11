from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.bank.models import CurrencyModel, CategoryModel, TransactionModel
from apps.bank.api.serializers import CurrencySerializer, CategorySerializer, TransactionSerializer

class CurrencyListAPIView(ListAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
    
# class CategoryListAPIView(ListAPIView):
#     queryset = CategoryModel.objects.all()
#     serializer_class = CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class TransactionModelViewSet(ModelViewSet):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer

class TransactionListAPIView(ListAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer