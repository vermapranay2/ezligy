# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20170331_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
