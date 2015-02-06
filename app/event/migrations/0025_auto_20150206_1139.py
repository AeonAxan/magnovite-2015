# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0024_registration_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['-created'], 'permissions': (('own_event_registrations', 'View registrations for own event'),)},
        ),
    ]
