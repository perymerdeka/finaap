from rest_framework.generics import ListAPIView

from apps.bank.models import CurrencyModel
from apps.bank.api.serializers import CurrencySerializer

class CurrencyListAPIView(ListAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer