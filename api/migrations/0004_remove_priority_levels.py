# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-06 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_received_at_to_locked_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskdef',
            name='priority_levels',
        )
    ]