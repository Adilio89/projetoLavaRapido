from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('agendamentos-do-dia/', views.agendamentos_do_dia, name='agendamentos_do_dia'),
    path('alterar-status/<int:agendamento_id>/<str:novo_status>/', views.alterar_status, name='alterar_status'),
]