# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateField(null=True)),
                ('dias_evaluacion', models.IntegerField(default=0, null=True)),
                ('tramite_tiempo', models.CharField(default=b'SI', max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('tipo_tramite', models.CharField(default=b'COFEMER', max_length=32, choices=[(b'COFEMER', b'COFEMER'), (b'IP', b'IP'), (b'MIA-P', b'MIA-P'), (b'MIA-P/ERA', b'MIA-P/ERA')])),
                ('bitacora', models.CharField(max_length=32)),
                ('numero_proyecto', models.CharField(max_length=32, null=True, blank=True)),
                ('estado_principal', models.CharField(max_length=64, null=True, blank=True)),
                ('estados', models.CharField(max_length=64, null=True, blank=True)),
                ('municipio', models.CharField(max_length=64, null=True, blank=True)),
                ('domicilio', models.CharField(max_length=255, null=True, blank=True)),
                ('nombre_proyecto', models.CharField(max_length=255, null=True, blank=True)),
                ('regulado', models.CharField(max_length=255, null=True, blank=True)),
                ('representante_legal', models.CharField(max_length=255, null=True, blank=True)),
                ('subsector', models.CharField(max_length=32, null=True, choices=[(b'PETR\xc3\x93LEO', b'PETR\xc3\x93LEO'), (b'PETROL\xc3\x8dFEROS', b'PETROL\xc3\x8dFEROS'), (b'GAS LP', b'GAS LP'), (b'GAS NATURAL', b'GAS NATURAL'), (b'RESIDUOS', b'RESIDUOS')])),
                ('tipo_instalacion', models.CharField(max_length=64, null=True, choices=[(b'EXPLORACI\xc3\x93N', b'EXPLORACI\xc3\x93N'), (b'ESTACI\xc3\x93N DE SERVICIO', b'ESTACI\xc3\x93N DE SERVICIO'), (b'ALMACENAMIENTO', b'ALMACENAMIENTO'), (b'TRANSPORTE', b'TRANSPORTE'), (b'PLANTA DE DISTRIBUCI\xc3\x93N', b'PLANTA DE DISTRIBUCI\xc3\x93N'), (b'DES DE DISTRIBUCI\xc3\x93N', b'RED DE DISTRIBUCI\xc3\x93N'), (b'PROSPECCI\xc3\x93N', b'PROSPECCI\xc3\x93N'), (b'DESCOMPRENSI\xc3\x93N DE GAS NATURAL', b'DESCOMPRENSI\xc3\x93N DE GAS NATURAL')])),
                ('ubicacion_instalacion', models.CharField(max_length=64, null=True, choices=[(b'CARRETERA', b'CARRETERA'), (b'URBANA', b'URBANA'), (b'NA', b'NA'), (b'ZONA URBANA', b'ZONA URBANA')])),
                ('evaluador', models.CharField(max_length=64, null=True)),
                ('fecha_asigna_evaluador', models.DateField(null=True)),
                ('situacion_actual', models.CharField(max_length=128, null=True, blank=True)),
                ('estatus', models.CharField(max_length=255, null=True, blank=True)),
                ('numero_resolucion', models.CharField(max_length=32, null=True, blank=True)),
                ('unidad_firma', models.CharField(max_length=16, null=True, blank=True)),
                ('fecha_emisi_resolu', models.DateField(null=True)),
                ('fecha_notifica_resolu', models.DateField(null=True)),
                ('sentido_resolucion', models.CharField(max_length=64, null=True, blank=True)),
                ('vigencia_resolucion', models.CharField(max_length=16, null=True, blank=True)),
                ('fecha_publica_extracto', models.DateField(null=True)),
                ('nume_of_apercibimiento', models.CharField(max_length=32, null=True, blank=True)),
                ('fecha_of_apercibimiento', models.DateField(null=True, blank=True)),
                ('fecha_notica_apercibimiento', models.DateField(null=True)),
                ('fecha_termi_apercibimiento', models.DateField(null=True)),
                ('fecha_entrega_apercibimiento', models.DateField(null=True)),
                ('dias_transcurre_apercibimiento', models.CharField(max_length=32, null=True, blank=True)),
                ('numero_of_infoadicional', models.CharField(max_length=32, null=True, blank=True)),
                ('fecha_of_infoadicional', models.DateField(null=True)),
                ('fecha_notifi_of_infoadicional', models.DateField(null=True)),
                ('fecha_vernci_of_infoadicional', models.DateField(null=True)),
                ('fecha_entrega_of_infoadicional', models.DateField(null=True)),
                ('dias_transcurre_of_infoadicional', models.IntegerField(default=0)),
                ('observasiones', models.CharField(max_length=512, null=True, blank=True)),
                ('numero_of_aplia_plazo', models.CharField(max_length=32, null=True, blank=True)),
                ('dias_emision_resolucion', models.IntegerField(default=0, null=True)),
                ('resolucion_tiempo', models.CharField(default=b'SI', max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('dia_actual', models.DateField(auto_now=True)),
                ('lati', models.FloatField(null=True, blank=True)),
                ('longi', models.FloatField(null=True, blank=True)),
                ('dias_feriado', models.DateField(null=True)),
                ('dias_habiles', models.DateField(null=True)),
                ('estatus_proyect', models.CharField(max_length=32, null=True, choices=[(b'CONSTRUIDA', b'CONSTRUIDA'), (b'EN CONSTRUCCI\xc3\x93N', b'EN CONSTRUCCI\xc3\x93N'), (b'OPERACI\xc3\x93N', b'OPERACI\xc3\x93N'), (b'NUEVA', b'NUEVA')])),
                ('llave_pago', models.CharField(max_length=32, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
