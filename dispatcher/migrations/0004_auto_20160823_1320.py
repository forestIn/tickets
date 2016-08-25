# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0003_auto_20160823_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='active',
        ),
        migrations.AddField(
            model_name='cars',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]