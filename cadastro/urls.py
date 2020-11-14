from django.urls import path
from .views import index
# from .views import cadastro

from .views import CampoCreate

urlpatterns = [
    path('', index),
    # path('cadastro/', cadastro),
    path('cadastro/', CampoCreate.as_view(), name='cadastro'),
]
