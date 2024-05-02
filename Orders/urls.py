from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing and creating orders
    # When the URL is accessed with a GET request, it lists all orders
    # When accessed with a POST request, it creates a new order
    path('', views.OrdersListCreate.as_view(), name='orders-list-create'),
    
    # URL pattern for retrieving, updating, and deleting orders by their primary key (pk)
    # <int:pk>/ specifies that the URL expects an integer value for the primary key
    # When accessed with a GET request, it retrieves the details of the order with the specified pk
    # When accessed with a PUT request, it updates the order with the specified pk
    # When accessed with a DELETE request, it deletes the order with the specified pk
    path('<int:pk>/', views.OrdersRetrieveUpdateDestroy.as_view(), name='orders-retrieve-update-destroy'),
]
