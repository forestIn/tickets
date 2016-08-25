# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 01:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0002_cars_be'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='be',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='res', to='users.BE', verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный за авто'),
        ),
    ]
