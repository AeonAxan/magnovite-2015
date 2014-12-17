# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20141217_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'permissions': (('own_event_registerations', 'View registrations for own event'),)},
        ),
    ]
