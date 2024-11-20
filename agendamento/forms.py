from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_proprietario', 'telefone', 'tipo_veiculo', 'modelo_veiculo', 'placa_veiculo', 'tipo_servico', 'status', 'data_agendamento']
