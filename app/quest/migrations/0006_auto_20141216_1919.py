# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0005_auto_20141216_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quest',
            options={'ordering': ['level']},
        ),
    ]
