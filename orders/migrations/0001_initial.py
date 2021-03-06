# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('price_total', models.DecimalField(decimal_places=2, default='95.00', max_digits=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
