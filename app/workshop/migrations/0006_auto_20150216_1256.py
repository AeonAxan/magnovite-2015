# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0005_workshop_registrations_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='registrations_open',
            field=models.BooleanField(default=True),
        ),
    ]
