# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20141203_1651'),
        ('main', '0006_auto_20141215_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='event',
        ),
        migrations.AddField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(related_name='heads', to='event.Event', null=True, help_text='The event this profile is in-charge of', blank=True),
            preserve_default=True,
        ),
    ]
