from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def verificar_feriados(request):
    dia_de_hoje = date.today()
    select_feriados = FeriadoModel.objects.all()
    mensagem_para_tela = 'Hoje não é feriado'

    for cursor_feriado in select_feriados: 
        if (cursor_feriado.dia == dia_de_hoje.day and cursor_feriado.mes == dia_de_hoje.month):
            mensagem_para_tela = 'Hoje temos um feriado, o feriado de hoje é: ' + cursor_feriado.nome
            
            EhFeriado = {
                'feriado_de_hoje' : mensagem_para_tela
            }

            return render(request, 'feriados.html', EhFeriado)
