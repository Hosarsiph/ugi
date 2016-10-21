# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0006_auto_20161019_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='municipio',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
