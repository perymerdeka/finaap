
from rest_framework.serializers import ModelSerializer, Serializer

from apps.bank.models import CurrencyModel, CategoryModel, TransactionModel

class CurrencySerializer(ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = TransactionModel
        # fields = '__all__'
        exclude = ['id']
        # fields = (
        #     "id",
        #     "amount",
        #     "currency",
        #     "date",
        #     "description",
        #     "category",
        # )