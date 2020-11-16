from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView
from cadastro.models import DadosClientes
from django.urls import reverse_lazy


class IndexView(ListView):
    models = DadosClientes
    template_name = 'index.html'
    queryset = DadosClientes.objects.all()
    context_object_name = 'clientes'


class ApiView(APIView):
    def get(self, request):
        dados = DadosClientes.objects.all()
        return Response({"api": dados})


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

