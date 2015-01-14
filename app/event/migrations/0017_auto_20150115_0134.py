# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_auto_20150108_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover',
            field=models.URLField(blank=True, default='', help_text='imgur link for cover (1300x500)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='picture_one',
            field=models.URLField(blank=True, default='', help_text='imgur link for head one (100x100)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture_two',
            field=models.URLField(blank=True, default='', help_text='imgur link for head one (100x100)'),
        ),
    ]
