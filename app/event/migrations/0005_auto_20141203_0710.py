# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20141203_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='team_max',
            field=models.IntegerField(default=1, help_text='Maximum number of people in a team (If individual: 1)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='team_min',
            field=models.IntegerField(default=1, help_text='Minimum number of people in a team (If individual: 1)'),
            preserve_default=True,
        ),
    ]
