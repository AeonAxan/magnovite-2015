# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20141203_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.CharField(max_length=30, blank=True, help_text='(End Time), Eg: 4:00 pm', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=30, blank=True, help_text='(Start time), Eg: 9:00 am'),
        ),
    ]
