from .views import UpdateClienteView, DeleteClienteView
from .views import IndexView, CreateClienteView
from cadastro.api import viewsets as cadastroviewset
from django.urls import path, include
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'cadastroapi', cadastroviewset.CadastroViewSet, basename='Cadastro')

urlpatterns = [
    path('', include(route.urls), name='cadastroapi'),
    path('index', IndexView.as_view(), name='index'),

    path('adicionar/', CreateClienteView.as_view(), name='adicionar_cliente'),
    path('<int:pk>/alterar/', UpdateClienteView.as_view(), name='atualizar_cliente'),
    path('<int:pk>/deletar/', DeleteClienteView.as_view(), name='deletar_cliente'),
]
