# Generated by Django 2.2.6 on 2019-10-21 21:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191022_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 21, 39, 58, 477143, tzinfo=utc)),
        ),
    ]
