# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20141215_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_active', models.BooleanField(default=False, help_text='If unchecked level wont be shown')),
                ('level', models.IntegerField(unique=True)),
                ('img1', models.URLField()),
                ('img2', models.URLField()),
                ('answer', models.CharField(max_length=50, help_text='Answer is case insensitive')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestScore',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('max_level', models.IntegerField(default=0)),
                ('max_time', models.DateTimeField()),
                ('profile', models.OneToOneField(to='main.Profile', related_name='quest_score')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
