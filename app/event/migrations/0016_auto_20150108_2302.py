# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20141217_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='quote',
            field=models.CharField(help_text='Text displayed on the cards in /events/', max_length=70),
        ),
    ]
