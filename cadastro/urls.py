from .views import UpdateClienteView, DeleteClienteView
from .views import IndexView, CreateClienteView, ApiView

from django.urls import path, include

from cadastro.api import viewsets as cadastroviewset
from rest_framework import routers


route = routers.DefaultRouter()
route.register(r'apicadastro', cadastroviewset.CadastroViewSet, basename='apicadastro')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include(route.urls)),
    path('api/', ApiView.as_view(), name='api'),

    # CRUD urls
    path('<int:pk>/alterar/', UpdateClienteView.as_view(), name='atualizar_cliente'),
    path('<int:pk>/deletar/', DeleteClienteView.as_view(), name='deletar_cliente'),
    path('adicionar/', CreateClienteView.as_view(), name='adicionar_cliente'),

]
