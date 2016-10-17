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
                ('fecha_ingreso', models.TextField(null=True, blank=True)),
                ('dias_evaluacion', models.TextField(null=True, blank=True)),
                ('tramite_tiempo', models.TextField(null=True, blank=True)),
                ('tipo_tramite', models.TextField(null=True, blank=True)),
                ('bitacora', models.TextField()),
                ('numero_proyecto', models.TextField(null=True, blank=True)),
                ('estado_principal', models.TextField(null=True, blank=True)),
                ('estados', models.TextField(null=True, blank=True)),
                ('municipio', models.TextField(null=True, blank=True)),
                ('domicilio', models.TextField(null=True, blank=True)),
                ('nombre_proyecto', models.TextField(null=True, blank=True)),
                ('regulado', models.TextField(null=True, blank=True)),
                ('representante_legal', models.TextField(null=True, blank=True)),
                ('subsector', models.TextField(null=True, blank=True)),
                ('tipo_instalacion', models.TextField(null=True, blank=True)),
                ('ubicacion_instalacion', models.TextField(null=True, blank=True)),
                ('evaluador', models.TextField(null=True, blank=True)),
                ('fecha_asigna_evaluador', models.TextField(null=True, blank=True)),
                ('situacion_actual', models.TextField(null=True, blank=True)),
                ('estatus', models.TextField(null=True, blank=True)),
                ('numero_resolucion', models.TextField(null=True, blank=True)),
                ('unidad_firma', models.TextField(null=True, blank=True)),
                ('fecha_emisi_resolu', models.TextField(null=True, blank=True)),
                ('fecha_notifica_resolu', models.TextField(null=True, blank=True)),
                ('sentido_resolucion', models.TextField(null=True, blank=True)),
                ('vigencia_resolucion', models.TextField(null=True, blank=True)),
                ('fecha_publica_extracto', models.TextField(null=True, blank=True)),
                ('nume_of_apercibimiento', models.TextField(null=True, blank=True)),
                ('fecha_of_apercibimiento', models.TextField(null=True, blank=True)),
                ('fecha_notica_apercibimiento', models.TextField(null=True, blank=True)),
                ('fecha_termi_apercibimiento', models.TextField(null=True, blank=True)),
                ('fecha_entrega_apercibimiento', models.TextField(null=True, blank=True)),
                ('dias_transcurre_apercibimiento', models.TextField(null=True, blank=True)),
                ('numero_of_infoadicional', models.TextField(null=True, blank=True)),
                ('fecha_of_infoadicional', models.TextField(null=True, blank=True)),
                ('fecha_notifi_of_infoadicional', models.TextField(null=True, blank=True)),
                ('fecha_vernci_of_infoadicional', models.TextField(null=True, blank=True)),
                ('fecha_entrega_of_infoadicional', models.TextField(null=True, blank=True)),
                ('dias_transcurre_of_infoadicional', models.TextField(null=True, blank=True)),
                ('observasiones', models.CharField(max_length=512, null=True, blank=True)),
                ('numero_of_aplia_plazo', models.TextField(null=True, blank=True)),
                ('dias_emision_resolucion', models.TextField(null=True, blank=True)),
                ('resolucion_tiempo', models.TextField(null=True, blank=True)),
                ('dia_actual', models.TextField(null=True, blank=True)),
                ('lati', models.TextField(null=True, blank=True)),
                ('longi', models.TextField(null=True, blank=True)),
                ('dias_feriado', models.TextField(null=True, blank=True)),
                ('dias_habiles', models.TextField(null=True, blank=True)),
                ('estatus_proyect', models.TextField(null=True, blank=True)),
                ('llave_pago', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
