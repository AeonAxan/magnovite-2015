# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='date_string',
            field=models.CharField(blank=True, max_length=50, help_text='Eg: From 20th to 21st of February', null=True),
            preserve_default=True,
        ),
    ]
