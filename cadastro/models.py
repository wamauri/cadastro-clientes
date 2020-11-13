from django.db import models


# Create your models here.
class DadosClientes(models.Model):
    nome = models.CharField('Nome', max_length=150, blank=True)
    telefone = models.CharField('Telefone', max_length=14, blank=True)
    email = models.EmailField('E-mail', max_length=50)
    data_nascimento = models.DateField('Data de Nascimento', max_length=10)

    cep = models.CharField('CEP', max_length=8)
    endereco = models.CharField('Endereço', max_length=100, blank=True)
    numero = models.CharField('Número', max_length=6)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    ponto_referencia = models.CharField('Ponto de Referêmcia', max_length=150)
