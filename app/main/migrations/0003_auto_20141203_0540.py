# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20141203_0503'),
        ('main', '0002_remove_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='event',
            field=models.ForeignKey(blank=True, to='event.Event', on_delete=django.db.models.deletion.SET_NULL, related_name='heads', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='is_internal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
