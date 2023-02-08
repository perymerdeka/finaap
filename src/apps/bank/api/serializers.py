
from rest_framework.serializers import ModelSerializer

from apps.bank.models import CurrencyModel, CategoryModel

class CurrencySerializer(ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
