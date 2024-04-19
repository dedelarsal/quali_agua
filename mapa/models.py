from django.conf import settings
from django.db import models
from django.utils import timezone


class Analise(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    concessionaria = models.CharField(max_length=200)
    municipio = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    data_analise = models.DateTimeField(blank=True, null=True)
    mes_referencia = models.CharField(max_length=2)
    ano_referencia = models.CharField(max_length=4)
    ponto_monitorado = models.CharField(max_length=50)
    parametro = models.CharField(max_length=50)
    valor_parametro = models.CharField(max_length=50)


    def publicacao(self):
        self.publicacao_data = timezone.now()
        self.save()

    def __str__(self):
        return self.parametro + ' - ' + self.municipio + ' - ' + self.rua
