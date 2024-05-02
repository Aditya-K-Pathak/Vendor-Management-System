from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.VendorProfileListCreate.as_view()),
    path('<str:pk>/', views.VendorProfileRetrieveUpdateDestroy.as_view()),
]
