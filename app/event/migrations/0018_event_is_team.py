# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_auto_20150115_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_team',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
