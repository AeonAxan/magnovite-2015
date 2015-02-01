# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_auto_20150201_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.IntegerField(help_text='20 or 21', max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
