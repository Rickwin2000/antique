from rest_framework import serializers
from antique_products.models.auction import AuctionModel
from antique_products.models.product import ProductModel
from antique_products.serializers.auction import AuctionSerializer
        

class MyListingSerializer(serializers.ModelSerializer):
    auctions = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductModel
        fields = "__all__"
    
    def get_auctions(self, obj):
        auctions = AuctionModel.objects.filter(product_id=obj.id)
        return AuctionSerializer(auctions, many=True).data