# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_auto_20141217_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'permissions': (('own_event_registrations', 'View registrations for own event'),)},
        ),
    ]
