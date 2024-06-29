from rest_framework import serializers
from antique_products.models.product import ProductModel
from antique_products.models.auction import AuctionModel
from django.db.models import Max


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductModel
        fields = "__all__"


class ProductPatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductModel
        fields = "__all__"


    def validate(self, data):
        id = self.instance.id
        status = data.get("status")
        if status in [False, "false"]:
            price = AuctionModel.objects.filter(product_id=id).aggregate(Max('price'))['price__max']
            self.instance.starting_price = price
            self.instance.save()
        return data