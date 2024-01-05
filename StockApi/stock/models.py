from django.db import models


class StockDB(models.Model):
    company_name = models.CharField(max_length=255)
    opening_price = models.BooleanField()
    closing_price = models.BooleanField()
    date = models.DateField(auto_now_add=True)
