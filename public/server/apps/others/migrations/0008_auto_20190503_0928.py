# Generated by Django 2.2.1 on 2019-05-03 09:28

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0007_auto_20190430_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerquestion',
            name='answer_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 9, 28, 37, 954871), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期'),
        ),
    ]