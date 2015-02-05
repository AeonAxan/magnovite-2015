# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import pytz

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_registration_on_spot'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 21, 42, 39, 842064, pytz.UTC), auto_now_add=True),
            preserve_default=False,
        ),
    ]
