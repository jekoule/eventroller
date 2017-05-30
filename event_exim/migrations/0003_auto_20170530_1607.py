# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_exim', '0002_auto_20170421_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='org2orgshare',
            name='status',
            field=models.IntegerField(choices=[(-1, 'disabled'), (0, 'offered'), (1, 'enabled')], default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='crm_type',
            field=models.CharField(choices=[('actionkit_api', 'actionkit_api'), ('actionkit_db', 'actionkit_db')], max_length=16),
        ),
    ]
