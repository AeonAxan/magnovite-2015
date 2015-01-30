# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150114_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pack',
            field=models.CharField(max_length=10, choices=[('none', 'No Pack'), ('single', 'Single Event Pack'), ('multiple', 'Multiple Event Pack')], default='none'),
            preserve_default=True,
        ),
    ]
