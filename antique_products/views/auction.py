from rest_framework import viewsets, permissions, status
from antique_products.models.auction import AuctionModel
from antique_products.serializers.auction import (
                            AuctionSerializer, 
                            AuctionCreateSerializer
                            )
from rest_framework.response import Response


class AuctionAPIView(viewsets.ModelViewSet):
    queryset = AuctionModel.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(auctioned_by=user)
            
    
    def create(self, request, *args, **kwargs):
        self.serializer_class = AuctionCreateSerializer
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)