# Generated by Django 2.2 on 2019-04-24 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190424_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 10, 35, 8, 207261)),
        ),
    ]
