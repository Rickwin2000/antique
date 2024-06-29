from django.urls import path
from antique_products.views.product import ProductAPIView
from antique_products.views.auction import AuctionAPIView
from antique_products.views.my_listing import MyListingAPIView


urlpatterns = [
    path('products/',ProductAPIView.as_view({'get': 'list', 'post': 'create'}), name='products'),
    path('products/<int:pk>/', ProductAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='products'),
    path('auctions/',AuctionAPIView.as_view({'post': 'create'}), name='auctions'),
    path('auctions/<int:pk>/', AuctionAPIView.as_view({'patch': 'partial_update'}), name='auctions'),
    path('my-listings/<int:pk>/', MyListingAPIView.as_view({'get': 'retrieve'}), name='my-listings'),
    path('my-listings/', MyListingAPIView.as_view({'get': 'list'}), name='my-listings'),
]