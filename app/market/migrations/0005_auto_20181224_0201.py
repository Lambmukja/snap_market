# Generated by Django 2.1.3 on 2018-12-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_market_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='working_time',
            field=models.TextField(default='', verbose_name='영업시간'),
        ),
    ]
