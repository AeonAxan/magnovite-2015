# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150204_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='on_spot',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='on_spot_payment',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='on_spot_registerer',
            field=models.CharField(default='', max_length=50, blank=True, null=True),
            preserve_default=True,
        ),
    ]
