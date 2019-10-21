# Generated by Django 2.2.6 on 2019-10-21 10:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191020_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_of_like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 10, 58, 20, 351888, tzinfo=utc)),
        ),
    ]