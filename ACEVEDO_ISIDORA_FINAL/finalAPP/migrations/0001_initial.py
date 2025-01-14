# Generated by Django 5.1 on 2024-12-20 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_personas', models.PositiveIntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_inscripcion', models.DateField()),
                ('hora_inscripcion', models.TimeField()),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], default='RESERVADO', max_length=20)),
                ('observaciones', models.CharField(blank=True, max_length=500)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalAPP.institucion')),
            ],
        ),
    ]
