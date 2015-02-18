# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0028_registration_mode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('change_own', 'Change events incharge of'),), 'ordering': ['-views']},
        ),
    ]
