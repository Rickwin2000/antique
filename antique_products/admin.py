# antique_products/admin.py

from django.contrib import admin
from antique_products.models.product import ProductModel

# Register your models here
admin.site.register(ProductModel)
