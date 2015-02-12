# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_auto_20150212_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='sulg',
            new_name='slug',
        ),
    ]
