# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141203_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='event',
            field=models.ForeignKey(null=True, help_text='The event this profile is in-charge of', on_delete=django.db.models.deletion.SET_NULL, to='event.Event', blank=True, related_name='heads'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_internal',
            field=models.BooleanField(help_text='Is this an internal account? (Event Heads, etc)', default=False),
        ),
    ]
