from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'product'

    def __str__(self):
        return f"Product - {self.id}"
