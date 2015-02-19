# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_profile_id_printed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='checked_in',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
