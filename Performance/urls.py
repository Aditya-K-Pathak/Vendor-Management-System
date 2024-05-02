from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/performance', views.PerformanceList.as_view()),
]
