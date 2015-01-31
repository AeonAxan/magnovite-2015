# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150130_2215'),
        ('event', '0018_event_is_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='team_owner',
            field=models.ForeignKey(to='main.Profile', blank=True, related_name='own_registrations', null=True),
            preserve_default=True,
        ),
    ]
