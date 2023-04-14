from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('feriado', max_length = 65)
    dia = models.IntegerField('data')
    mes = models.IntegerField('mes')
    modificado_em = models.DateTimeField(
        verbose_name = 'ultima alteracao foi em:', 
        auto_now_add = False, auto_now = True
    )

    def __str__(self):
        return self.nome
