# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150205_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='receipt_id',
            field=models.CharField(blank=True, max_length=100, null=True),
            preserve_default=True,
        ),
    ]
