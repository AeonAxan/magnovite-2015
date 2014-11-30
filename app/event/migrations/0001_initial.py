# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(help_text='The event url, use all simple and - as a seperator, Eg: junkyard-wars')),
                ('quote', models.CharField(max_length=50, help_text='Text displayed on the cards in /events/')),
                ('info', models.TextField(help_text='Please write in Markdown (Use headings, bold, italic, lists)')),
                ('cash_prize', models.IntegerField(help_text='Numeric, Eg: 5000')),
                ('date', models.IntegerField(max_length=2, help_text='Eg: 21')),
                ('time', models.CharField(max_length=30, help_text='(Start time), Eg: 2pm')),
                ('venue', models.CharField(max_length=50, help_text='Eg: Room 243, Block 2')),
                ('technical', models.BooleanField(default=True, help_text='If cultural set to false')),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('CSE', 'Computer Science'), ('EC', 'Electronics'), ('MECH', 'Mechanical'), ('CIVIL', 'Civil')], max_length=17, null=True, blank=True)),
                ('cover_picture', models.ImageField(upload_to='covers/', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_id', models.IntegerField(null=True, blank=True)),
                ('event', models.ForeignKey(to='event.Event')),
                ('profile', models.ForeignKey(to='main.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
