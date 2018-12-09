# Generated by Django 2.1.3 on 2018-12-09 13:58

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_market_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='contract_idxs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='market',
            name='photographer_idx',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='사진작가 idx'),
        ),
        migrations.AlterField(
            model_name='market',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='market',
            name='working_time',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='영업시간'),
        ),
    ]