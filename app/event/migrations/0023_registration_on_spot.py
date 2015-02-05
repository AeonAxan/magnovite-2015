# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_auto_20150202_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='on_spot',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
