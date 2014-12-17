# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('data', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
