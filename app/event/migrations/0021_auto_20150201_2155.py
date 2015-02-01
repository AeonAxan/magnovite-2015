# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_auto_20150131_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_team',
        ),
        migrations.AddField(
            model_name='event',
            name='team_type',
            field=models.CharField(default='individual', max_length=20, choices=[('individual', 'Individual'), ('team', 'Team'), ('group', 'Group')]),
            preserve_default=True,
        ),
    ]
