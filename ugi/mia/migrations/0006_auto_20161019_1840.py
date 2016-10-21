# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0005_auto_20161019_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='domicilio',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mia',
            name='estatus',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mia',
            name='nombre_proyecto',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mia',
            name='regulado',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mia',
            name='representante_legal',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
    ]
