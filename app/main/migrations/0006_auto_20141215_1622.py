# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141215_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='is_staff',
            field=models.BooleanField(help_text='Has access to admin site', default=False),
        ),
    ]
