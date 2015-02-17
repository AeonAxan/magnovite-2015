# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_profile_hospitality_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='remarks',
            field=models.TextField(default='', blank=True, null=True),
            preserve_default=True,
        ),
    ]
