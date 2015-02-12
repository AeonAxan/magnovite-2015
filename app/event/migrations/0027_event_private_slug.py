# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0026_remove_event_registrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='private_slug',
            field=models.CharField(max_length=40, blank=True, default=''),
            preserve_default=True,
        ),
    ]
