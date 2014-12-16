# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0003_auto_20141216_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='level',
            field=models.IntegerField(unique=True),
        ),
    ]
