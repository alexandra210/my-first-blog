# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-08 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20190107_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название', models.CharField(max_length=200)),
                ('Форма_выпуска', models.TextField()),
                ('Дозировка', models.CharField(max_length=200)),
                ('Ваш_email', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]