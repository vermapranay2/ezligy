# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20170331_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('cost', models.CharField(max_length=100)),
                ('defination', tinymce.models.HTMLField()),
                ('video', models.FileField(upload_to='')),
                ('features', tinymce.models.HTMLField()),
                ('benefits', tinymce.models.HTMLField()),
                ('limitations', tinymce.models.HTMLField()),
                ('procedure', tinymce.models.HTMLField()),
                ('documents', tinymce.models.HTMLField()),
                ('faqs', tinymce.models.HTMLField()),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.Service')),
            ],
        ),
    ]
