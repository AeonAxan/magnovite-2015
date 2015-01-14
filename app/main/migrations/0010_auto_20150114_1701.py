# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20141217_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='year',
        ),
        migrations.AddField(
            model_name='profile',
            name='referral',
            field=models.CharField(max_length=50, default='', help_text='Referral: How did you find out about us?', blank=True),
            preserve_default=True,
        ),
    ]
