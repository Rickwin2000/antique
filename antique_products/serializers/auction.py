from rest_framework import serializers
from antique_products.models.product import ProductModel

from antique_products.models.auction import AuctionModel


class AuctionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuctionModel
        fields = "__all__"
        
        

class AuctionCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuctionModel
        fields = "__all__"

    def validate_product_id(self, data):
        if data.status in ['false', False]:
            raise serializers.ValidationError("Already bid get closed")
        
        product_created = ProductModel.objects.get(id=data.id).created_by.id
        user_id = self.context["request"].user.id
        if product_created == user_id:
            raise serializers.ValidationError("You cannot auction your own product.")
        return data
    
    
    def validate_price(self, data):
        product_id = self.initial_data.get("product_id")
        product = ProductModel.objects.filter(id=product_id).first()
        if product and data and data < product.starting_price:
            raise serializers.ValidationError("Amount is lesser than starting price")
        auctions = AuctionModel.objects.filter(product_id=product_id)
        for auction in auctions:
            if auction and data <= auction.price:
                raise serializers.ValidationError("Amount is lesser than already bided price")
        return data