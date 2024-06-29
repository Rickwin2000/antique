from rest_framework import viewsets, permissions, status
from django.shortcuts import get_object_or_404
from antique_products.models.product import ProductModel
from antique_products.serializers.product import ProductSerializer, ProductPatchSerializer
from rest_framework.response import Response


class ProductAPIView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            current_user = self.request.user
            return self.queryset.exclude(created_by=current_user)
        else:
            current_user = self.request.user
            return self.queryset.filter(created_by=current_user)
            

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    def partial_update(self, request, *args, **kwargs):
        self.serializer_class = ProductPatchSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(instance)
        return Response({"detail": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
