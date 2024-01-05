from rest_framework import generics
from .models import StockDB
from .serializers import StockDBSerializer


class StockDBListView(generics.ListAPIView):
    queryset = StockDB.objects.all()
    serializer_class = StockDBSerializer
