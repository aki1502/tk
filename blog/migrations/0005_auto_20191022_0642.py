# Generated by Django 2.2.6 on 2019-10-21 21:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191022_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 21, 42, 3, 401838, tzinfo=utc)),
        ),
    ]
