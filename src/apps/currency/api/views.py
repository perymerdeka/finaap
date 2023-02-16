from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


from modules.floatrates.spider import FloatratesSpider
from .serializers import CurrencyScraperSerializer

class CurrencyScraperViewSet(ViewSet):
    def list(self, request):
        url= f"http://www.floatrates.com/daily/usd.json"
        spider = FloatratesSpider(url=url)
        queryset = spider.parse()
        serializer = CurrencyScraperSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, currency, code):
        url= f"http://www.floatrates.com/daily/{currency}.json"
        spider = FloatratesSpider(url=url)
        queryset = spider.parse(key=code)
        serializer = CurrencyScraperSerializer(queryset)
        return Response(serializer.data)
        