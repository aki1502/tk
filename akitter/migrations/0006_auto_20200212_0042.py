# Generated by Django 2.2.6 on 2020-02-11 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('akitter', '0005_auto_20191027_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akeet',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 15, 42, 22, 44697, tzinfo=utc)),
        ),
    ]