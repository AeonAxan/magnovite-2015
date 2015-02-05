# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_profile_registered_workshops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registered_workshops',
            field=models.ManyToManyField(null=True, to='workshop.Workshop', blank=True),
        ),
    ]
