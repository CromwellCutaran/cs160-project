# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SC_produce',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image_path', models.CharField(max_length=5000)),
                ('category', models.CharField(max_length=100)),
                ('amount_left', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SM_produce',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image_path', models.CharField(max_length=5000)),
                ('category', models.CharField(max_length=100)),
                ('amount_left', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
