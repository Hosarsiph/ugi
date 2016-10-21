# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='resolucion_tiempo',
            field=models.CharField(default=b'SI', max_length=2, null=True, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
        migrations.AlterField(
            model_name='mia',
            name='tipo_tramite',
            field=models.CharField(default=b'COFEMER', max_length=32, null=True, choices=[(b'COFEMER', b'COFEMER'), (b'IP', b'IP'), (b'MIA-P', b'MIA-P'), (b'MIA-P/ERA', b'MIA-P/ERA')]),
        ),
        migrations.AlterField(
            model_name='mia',
            name='tramite_tiempo',
            field=models.CharField(default=b'SI', max_length=2, null=True, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
    ]
