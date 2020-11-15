from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from cadastro.models import DadosClientes
from django.urls import reverse_lazy


class IndexView(ListView):
    models = DadosClientes
    template_name = 'index.html'
    queryset = DadosClientes.objects.all()
    context_object_name = 'clientes'


class CreateClienteView(CreateView):
    model = DadosClientes
    template_name = 'add_cliente.html'
    fields = [
        'nome',
        'email',
        'telefone',
        'data_nascimento',
        'cep',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'ponto_referencia',
    ]
    success_url = reverse_lazy('index')


class UpdateClienteView(UpdateView):
    model = DadosClientes
    template_name = 'add_cliente.html'
    fields = [
        'nome',
        'email',
        'telefone',
        'data_nascimento',
        'cep',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'ponto_referencia',
    ]
    success_url = reverse_lazy('index')


class DeleteClienteView(DeleteView):
    model = DadosClientes
    template_name = 'del_cliente.html'
    success_url = reverse_lazy('index')


# class CadastroApi(TemplateView):
#     template_name = 'cadastroapi.html'


# class CampoCreate(CreateView):
#     model = DadosClientes
#     fields = [
#         'nome',
#         'email',
#         'telefone',
#         'data_nascimento',
#         'cep',
#         'logradouro',
#         'numero',
#         'bairro',
#         'cidade',
#         'estado',
#         'ponto_referencia',
#     ]
#     template_name = 'cadastro.html'
#     success_url = reverse_lazy('cadastro')
