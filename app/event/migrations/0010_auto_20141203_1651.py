# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20141203_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='info',
            field=models.TextField(help_text='Please write in Markdown (Editor: http://dillinger.io/)'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_id',
            field=models.CharField(max_length=5, blank=True, null=True),
        ),
    ]
