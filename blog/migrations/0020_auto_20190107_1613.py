# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-07 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_post_наличие'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Наличие',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='Противопоказания',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='Срок_годности',
            field=models.CharField(max_length=30),
        ),
    ]
