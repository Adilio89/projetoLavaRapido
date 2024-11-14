from django.shortcuts import render
from django.utils import timezone
from .models import Agendamento


def index(request):
    return render(request, 'agendamento/index.html')


def agendamentos_do_dia(request):
    data_atual = timezone.now().date()
    agendamentos = Agendamento.objects.filter(data_agendamento__date = data_atual)

    return render(request, 'agendamento/agendamentos_do_dia.html', {'agendamentos': agendamentos})