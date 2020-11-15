from .views import CampoCreate, UpdateClienteView, DeleteClienteView
from .views import IndexView, CadastroApi, CreateClienteView
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CampoCreate.as_view(), name='cadastro'),
    path('cadastroapi/', CadastroApi.as_view(), name='cadastroapi'),

    path('adicionar/', CreateClienteView.as_view(), name='adicionar_cliente'),
    path('<int:pk>/alterar/', UpdateClienteView.as_view(), name='atualizar_cliente'),
    path('<int:pk>/deletar/', DeleteClienteView.as_view(), name='deletar_cliente'),
]
