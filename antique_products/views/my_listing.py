from rest_framework import viewsets, permissions, status
from django.shortcuts import get_object_or_404
from antique_products.models.product import ProductModel
from antique_products.serializers.my_listing import MyListingSerializer
from rest_framework.response import Response


class MyListingAPIView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = MyListingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        current_user = self.request.user
        return self.queryset.filter(created_by=current_user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)