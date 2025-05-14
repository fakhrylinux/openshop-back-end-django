from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=16)
    description = models.TextField()
    shop = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length=100)
    stock = models.IntegerField()
    is_available = models.BooleanField()
    picture = models.CharField(max_length=100)
