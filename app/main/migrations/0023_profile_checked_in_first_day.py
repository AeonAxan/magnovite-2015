# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_profile_checked_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='checked_in_first_day',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
