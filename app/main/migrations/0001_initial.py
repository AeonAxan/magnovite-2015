# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Magnovite User',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('auth_provider', models.CharField(blank=True, max_length=30)),
                ('active_email', models.EmailField(max_length=75)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(help_text='Without +91', blank=True, max_length=10)),
                ('college', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('year', models.IntegerField(help_text='Studying in year (1, 2, 3, 4, 5)?', blank=True, max_length=1, null=True)),
                ('registered_events', models.ManyToManyField(to='event.Event', through='event.Registration')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
