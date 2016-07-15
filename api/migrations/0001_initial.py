# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 03:43
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock_id', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending_queue', 'Pending Queue'), ('scheduled', 'Scheduled'), ('queued', 'Queued'), ('in_progress', 'In Progress'), ('failed_retrying', 'Failed - Retrying'), ('dequeued', 'Dequeued'), ('failed', 'Failed'), ('completed', 'Completed')], max_length=17)),
                ('received_at', models.DateTimeField()),
                ('priority', models.CharField(choices=[('critical', 'Critical'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low')], max_length=8)),
                ('unique', models.CharField(max_length=255)),
                ('run_at', models.DateTimeField()),
                ('run_every', models.CharField(max_length=255)),
                ('recurring_run_enabled', models.NullBooleanField()),
                ('started_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField()),
                ('failed_at', models.DateTimeField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('attempts', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority_levels', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('default_timeout', models.IntegerField(default=600)),
                ('max_attempts', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'task_defs',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='task_def_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TaskDef'),
        ),
    ]
