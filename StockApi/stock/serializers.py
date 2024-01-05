from rest_framework import serializers
from .models import StockDB


class StockDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDB
        fields = '__all__'
