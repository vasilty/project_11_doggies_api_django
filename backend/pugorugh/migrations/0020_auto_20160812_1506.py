# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-12 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0019_auto_20160812_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]