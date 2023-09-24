from django.urls import path
from weddingapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
