# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20141219_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='should_email',
            field=models.BooleanField(default=False, help_text='If checked, the user will be emailed notifying about this reply'),
            preserve_default=True,
        ),
    ]
