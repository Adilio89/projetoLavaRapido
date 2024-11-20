from django.db import models
from datetime import datetime


class Agendamento(models.Model):
    TIPO_VEICULO_CHOICES = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('caminhonete', 'Caminhonete'),
    ]

    TIPO_SERVICO_CHOICES = [
        ('basico', 'Lavagem Básica'),
        ('completa', 'Lavagem Completa'),
        ('polimento', 'Polimento'),
        ('enceramento', 'Enceramento'),
    ]
    STATUS_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]

    nome_proprietario = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    tipo_veiculo = models.CharField(max_length=25, choices=TIPO_VEICULO_CHOICES)
    modelo_veiculo = models.CharField(max_length=100)
    placa_veiculo = models.CharField(max_length=10)
    tipo_servico = models.CharField(max_length=25, choices=TIPO_SERVICO_CHOICES)
    data_agendamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aguardando'
    )

    @property
    def horario_agendado(self):
        if self.data_agendamento:
            return self.data_agendamento.strftime("%H:%M")
        return "Horário não definido"

    def __str__(self):
        horario = self.horario_agendado or "Sem horário"
        return f"{self.nome_proprietario} - {self.tipo_servico} no {self.modelo_veiculo} agendado em {self.data_agendamento}"
