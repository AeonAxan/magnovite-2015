# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='header_text',
            field=models.CharField(blank=True, max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quest',
            name='img1_desc',
            field=models.CharField(blank=True, max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quest',
            name='img2_desc',
            field=models.CharField(blank=True, max_length=100, default=''),
            preserve_default=True,
        ),
    ]
