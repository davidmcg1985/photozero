# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-timestamp', '-updated']},
        ),
    ]
