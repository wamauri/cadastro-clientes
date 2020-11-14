from django.shortcuts import render

from cadastro.models import DadosClientes
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html')


class CampoCreate(CreateView):
    model = DadosClientes
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
    template_name = 'cadastro.html'
    success_url = reverse_lazy('cadastro')
