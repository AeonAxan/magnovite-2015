# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_profile_receipt_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hospitality_days',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
