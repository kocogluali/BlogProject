# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20160825_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='seo_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
