# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-07 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190107_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitamin',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='Наличие',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='Противопоказания',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='Способ_применения',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='Срок_годности',
        ),
        migrations.RemoveField(
            model_name='vitamin',
            name='Форма_выпуска',
        ),
        migrations.AlterField(
            model_name='vitamin',
            name='Вкус',
            field=models.CharField(max_length=100),
        ),
    ]