# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20141203_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.IntegerField(help_text='Eg: 21', max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(help_text='(Start time), Eg: 2pm', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(help_text='Eg: Room 243, Block 2', max_length=50, blank=True),
        ),
    ]
