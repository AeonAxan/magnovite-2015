# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
        ('main', '0013_auto_20150203_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='registered_workshops',
            field=models.ManyToManyField(to='workshop.Workshop'),
            preserve_default=True,
        ),
    ]
