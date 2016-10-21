# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0002_auto_20161019_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='dias_transcurre_of_infoadicional',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
