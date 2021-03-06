# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 05:25
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(max_length=100, verbose_name='스튜디오 이름')),
                ('posts', models.TextField(blank=True, null=True, verbose_name='게시글')),
                ('working_time', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='영업시간')),
                ('costs', models.PositiveIntegerField(verbose_name='가격')),
                ('kakao_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='카카오톡 ID')),
                ('photographer_idx', models.PositiveSmallIntegerField(verbose_name='사진작가 idx')),
                ('contract_idxs', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None)),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='위치')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='전화번호')),
            ],
        ),
    ]
