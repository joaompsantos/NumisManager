# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coinmanager', '0003_auto_20151227_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='entry_date',
        ),
    ]
