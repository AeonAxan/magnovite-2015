# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141215_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 12, 17, 16, 29, 53, 574736)),
            preserve_default=False,
        ),
    ]
