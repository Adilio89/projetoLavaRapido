# Generated by Django 5.1.3 on 2024-11-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_proprietario', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('tipo_veiculo', models.CharField(choices=[('carro', 'Carro'), ('moto', 'Moto'), ('caminhonete', 'Caminhonete')], max_length=25)),
                ('modelo_veiculo', models.CharField(max_length=100)),
                ('placa_veiculo', models.CharField(max_length=10)),
                ('tipo_servico', models.CharField(choices=[('basico', 'Lavagem Básica'), ('completa', 'Lavagem Completa'), ('polimento', 'Polimento'), ('enceramento', 'Enceramento')], max_length=25)),
                ('data_agendamento', models.DateTimeField()),
            ],
        ),
    ]