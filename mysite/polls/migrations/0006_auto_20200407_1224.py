# Generated by Django 3.0.3 on 2020-04-07 03:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200407_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 3, 24, 44, 100117, tzinfo=utc)),
        ),
    ]
