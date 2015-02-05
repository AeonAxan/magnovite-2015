# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150205_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='on_spot_payment',
            new_name='total_payment',
        ),
    ]
