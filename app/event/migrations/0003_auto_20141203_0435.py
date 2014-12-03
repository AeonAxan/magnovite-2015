# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_registration_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cse', 'Computer Science'), ('ec', 'Electronics'), ('mech', 'Mechanical'), ('civil', 'Civil')], null=True, max_length=17),
        ),
    ]
