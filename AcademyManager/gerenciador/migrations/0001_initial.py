# Generated by Django 4.0.5 on 2022-06-11 04:18

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.IntegerField(unique=True)),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14, verbose_name='CPF')),
            ],
        ),
    ]
