from django.urls import path

from .views import index
from .views import cadastro

urlpatterns = [
    path('', index),
    path('cadastro/', cadastro),
]
