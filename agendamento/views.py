import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Agendamento


def index(request):
    return render(request, 'agendamento/index.html')


def agendamentos_do_dia(request):
    agendamentos = Agendamento.objects.filter(data_agendamento__date = datetime.date.today())
    return render(request, 'agendamento/agendamentos_do_dia.html', {'agendamentos': agendamentos})


@require_POST
def alterar_status(request, agendamento_id, novo_status):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.status = novo_status
    agendamento.save()
    return redirect('agendamentos_do_dia')