import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import now


def index(request):
    return render(request, 'agendamento/index.html')


def agendamentos_do_dia(request):
    if request.method == 'POST':
        agendamentos = Agendamento.objects.all()
    else:
        agendamentos = Agendamento.objects.filter(data_agendamento__date=datetime.date.today())
    return render(request, 'agendamento/agendamentos_do_dia.html', {'agendamentos': agendamentos})


@require_POST
def alterar_status(request, agendamento_id, novo_status):
    if request.method == "POST":
        agendamento = get_object_or_404(Agendamento, id=agendamento_id)
        agendamento.status = novo_status
        agendamento.save()
        return redirect('agendamentos_do_dia')


def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o agendamento no banco de dados
            return redirect('agendamentos_do_dia')  # Redireciona para a lista de agendamentos do dia
    else:
        form = AgendamentoForm()  # Cria um formulário vazio para GET
    return render(request, 'agendamento/agendar.html', {'form': form})


def minha_view(request):
    messages.success(request, "Agendamento realizado com sucesso!")
    return render(request, 'index.html')


def concluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    # Atualize o status e registre a hora de término
    agendamento.status = 'concluido'
    agendamento.horario_termino = now()
    agendamento.save()

    return redirect('agendamentos_do_dia')