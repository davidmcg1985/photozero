# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0026_auto_20160203_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-timestamp', '-updated']},
        ),
    ]
