# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_profile_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_printed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
