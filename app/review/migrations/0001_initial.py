# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_idx', models.PositiveSmallIntegerField()),
                ('market_idx', models.PositiveSmallIntegerField()),
                ('stars', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='별점')),
                ('review', models.TextField(verbose_name='리뷰')),
            ],
        ),
    ]
