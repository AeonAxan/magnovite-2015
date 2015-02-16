# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_auto_20150212_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='registrations_open',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
