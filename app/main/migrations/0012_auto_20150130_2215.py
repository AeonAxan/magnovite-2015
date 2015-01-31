# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_profile_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pack',
            field=models.CharField(default='none', choices=[('none', 'No Pack'), ('single', 'Single Event Pack'), ('multiple', 'Multiple Events Pack')], max_length=10),
        ),
    ]
