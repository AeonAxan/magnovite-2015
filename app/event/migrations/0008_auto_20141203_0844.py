# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_event_picture_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture_two',
            field=models.BooleanField(help_text='Does event head 2 have a picture? (name: img/events/<slug>_h2.jpg)', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='picture_one',
            field=models.BooleanField(help_text='Does event head 1 have a picture? (name: img/events/<slug>_h1.jpg)', default=False),
        ),
    ]
