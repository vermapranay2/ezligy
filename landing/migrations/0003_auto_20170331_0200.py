# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-30 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_service_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.URLField(default=None, null=True),
        ),
    ]
