# Generated by Django 2.2 on 2019-04-24 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_auto_20190424_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 15, 25, 13, 775502), verbose_name='日期'),
        ),
    ]
