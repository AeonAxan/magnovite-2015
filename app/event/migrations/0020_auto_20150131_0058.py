# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_registration_team_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='team_owner',
        ),
        migrations.AddField(
            model_name='registration',
            name='is_owner',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
