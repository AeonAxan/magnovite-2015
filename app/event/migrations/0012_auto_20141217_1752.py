# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20141217_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registrations',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
