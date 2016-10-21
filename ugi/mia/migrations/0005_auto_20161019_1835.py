# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0004_auto_20161019_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='numero_resolucion',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
