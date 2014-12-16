# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0004_auto_20141216_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questscore',
            name='max_level',
            field=models.IntegerField(default=1),
        ),
    ]
