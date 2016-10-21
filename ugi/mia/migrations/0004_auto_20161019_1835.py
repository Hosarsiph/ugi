# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0003_auto_20161019_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='nume_of_apercibimiento',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
