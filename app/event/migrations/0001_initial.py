# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('quote', models.CharField(max_length=50)),
                ('info', models.TextField(help_text='Please write in Markdown')),
                ('cash_prize', models.IntegerField()),
                ('time', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=50)),
                ('technical', models.BooleanField(default=True)),
                ('tags', models.CharField(blank=True, help_text='Comma seperated list of tags', max_length=100, null=True)),
                ('cover_picture', models.ImageField(blank=True, upload_to='covers/', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
