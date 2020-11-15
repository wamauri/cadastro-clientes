from django.contrib import admin
from .models import DadosClientes


# @admin.register(DadosClientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = (
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
    )


admin.site.register(DadosClientes, ClientesAdmin)
