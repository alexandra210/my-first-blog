# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-07 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190107_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Противопоказания_к_применению',
        ),
    ]
