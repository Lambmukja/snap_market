# Generated by Django 2.1.3 on 2018-12-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]