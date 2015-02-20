# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0029_auto_20150218_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reg_closed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
