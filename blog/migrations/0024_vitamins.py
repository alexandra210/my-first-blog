# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-07 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0023_medicine_выдача'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitamins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название', models.CharField(max_length=200)),
                ('Вкус', models.CharField(max_length=200)),
                ('Форма_выпуска', models.TextField()),
                ('Способ_применения', models.TextField()),
                ('Противопоказания', models.CharField(max_length=500)),
                ('Срок_годности', models.CharField(max_length=30)),
                ('Наличие', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
