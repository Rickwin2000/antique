from rest_framework import viewsets, permissions, status
from antique_products.models.auction import AuctionModel
from antique_products.serializers.auction import (
                            AuctionSerializer, 
                            AuctionCreateSerializer, 
                            AuctionPatchSerializer
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
    
    def partial_update(self, request, *args, **kwargs):
        self.serializer_class = AuctionPatchSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)