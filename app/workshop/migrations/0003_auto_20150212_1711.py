# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_workshop_date_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='private_slug',
            field=models.CharField(default='', blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workshop',
            name='sulg',
            field=models.CharField(default='', blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
    ]
