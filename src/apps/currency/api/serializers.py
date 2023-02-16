from rest_framework import serializers

class CurrencyScraperSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)
    alphaCode = serializers.CharField(max_length=5)
    numericCode = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    
    numericCode = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    rate = serializers.DecimalField(max_digits=16, decimal_places=2)
    date = serializers.DateField()
    inverseRate = serializers.DecimalField(max_digits=16, decimal_places=2)

