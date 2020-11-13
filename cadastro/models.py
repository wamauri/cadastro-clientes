from django.db import models


# Create your models here.
class DadosClientes(models.Model):
    nome = models.CharField('Nome', max_length=150, blank=True)
    telefone = models.CharField('Telefone', max_length=14, blank=True)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField(max_length=10)

    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100, blank=True)
    ponto_referencia = models.CharField(max_length=150)
