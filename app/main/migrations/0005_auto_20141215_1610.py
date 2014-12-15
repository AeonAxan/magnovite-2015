# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('main', '0004_auto_20141203_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', related_name='user_set', blank=True, verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='muser',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='muser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', blank=True, verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
