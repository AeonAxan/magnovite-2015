# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0027_event_private_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='mode',
            field=models.CharField(default='online', null=True, max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
