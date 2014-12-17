# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_muser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='heads', null=True, to='event.Event', verbose_name='Events Incharge of', help_text='The event this profile is in-charge of'),
        ),
    ]
