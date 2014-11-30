# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='profile',
            field=models.ForeignKey(to='main.Profile'),
            preserve_default=True,
        ),
    ]
