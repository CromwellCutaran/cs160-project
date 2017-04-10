# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170409_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(choices=[('Santa Clara', 'Santa Clara'), ('San Mateo', 'San Mateo')], default='Santa Clara', max_length=2),
        ),
    ]