# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-14 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0021_auto_20160814_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]