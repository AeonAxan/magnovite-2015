# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0002_auto_20141216_0831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questscore',
            options={'ordering': ['sort_key']},
        ),
        migrations.RemoveField(
            model_name='quest',
            name='is_active',
        ),
        migrations.AddField(
            model_name='questscore',
            name='sort_key',
            field=models.CharField(blank=True, max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quest',
            name='img1',
            field=models.URLField(help_text='Imgur direct JPG url, 250x250 px'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='img2',
            field=models.URLField(help_text='Imgur direct JPG url, 250x250 px'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='level',
            field=models.CharField(max_length=20, unique=True, help_text='level name (eg: Level 1)'),
        ),
    ]
