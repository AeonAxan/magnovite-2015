# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(help_text='The event url, use all simple and - as a seperator, Eg: junkyard-wars')),
                ('quote', models.CharField(help_text='Text displayed on the cards in /events/', max_length=50)),
                ('info', models.TextField(help_text='Please write in Markdown (Use headings, bold, italic, lists)')),
                ('cash_prize', models.IntegerField(help_text='Numeric, Eg: 5000')),
                ('date', models.IntegerField(help_text='Eg: 21', max_length=2)),
                ('time', models.CharField(help_text='(Start time), Eg: 2pm', max_length=30)),
                ('venue', models.CharField(help_text='Eg: Room 243, Block 2', max_length=50)),
                ('technical', models.BooleanField(help_text='If cultural set to false', default=True)),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('CSE', 'Computer Science'), ('EC', 'Electronics'), ('MECH', 'Mechanical'), ('CIVIL', 'Civil')], blank=True, max_length=17, null=True)),
                ('cover_picture', models.ImageField(blank=True, upload_to='covers/', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('team_id', models.IntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
