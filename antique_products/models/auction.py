from django.db import models
from antique_products.models.product import ProductModel
from django.contrib.auth.models import User
from django.utils import timezone


class AuctionModel(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    price = models.FloatField()
    auctioned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'auction'
        
    def __str__(self):
        return f"Auction - {self.id}"
