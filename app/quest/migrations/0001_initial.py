# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150130_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('level', models.IntegerField(unique=True)),
                ('img1', models.URLField(help_text='Imgur direct JPG url, 250x250 px')),
                ('img2', models.URLField(help_text='Imgur direct JPG url, 250x250 px')),
                ('answer', models.CharField(help_text='Answer is case insensitive', max_length=50)),
            ],
            options={
                'ordering': ['level'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('max_level', models.IntegerField(default=1)),
                ('max_time', models.DateTimeField()),
                ('sort_key', models.CharField(blank=True, max_length=20, null=True)),
                ('profile', models.OneToOneField(to='main.Profile', related_name='quest_score')),
            ],
            options={
                'ordering': ['-sort_key'],
            },
            bases=(models.Model,),
        ),
    ]
