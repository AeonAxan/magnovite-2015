# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questscore',
            options={'ordering': ['-max_level', 'max_time']},
        ),
    ]
